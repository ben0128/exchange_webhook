from pymongo import MongoClient
import asyncio
import httpx
from bs4 import BeautifulSoup
import schedule
import time
import concurrent.futures
import nest_asyncio

nest_asyncio.apply()

mongo_url = "process_env_mongo_url"
client = MongoClient(mongo_url)
db = client.test
orders_collection = db.orders
users_collection = db.users

executor = concurrent.futures.ThreadPoolExecutor()

def sync_complete_limit_order(order_id, order_type):
    with client.start_session() as session:
        with session.start_transaction():
            if order_type == "buy":
                orders_collection.update_one({"_id": order_id}, {"$set": {"state": "completed"}}, session=session)
            elif order_type == "sell":
                completed_order = orders_collection.find_one_and_update(
                    {"_id": order_id},
                    {"$set": {"state": "completed"}},
                    return_document=pymongo.ReturnDocument.AFTER,
                    session=session
                )
                # 更新用戶餘額
                users_collection.update_one(
                    {"_id": completed_order['userId']},
                    {"$inc": {"account": completed_order['shares'] * completed_order['price']}},
                    session=session
                )

async def complete_limit_order(order_id, order_type):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(executor, sync_complete_limit_order, order_id, order_type)

async def fetch_stock_price():
    pending_orders = orders_collection.find({"state": "pending"})
    async with httpx.AsyncClient() as client:
        for order in pending_orders:
            print(order)
            url = f'https://tw.stock.yahoo.com/quote/{order["targetName"]}'
            response = await client.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            price_div = soup.find('div', class_='D(f) Ai(fe) Mb(4px)')
            price = float(price_div.find('span').text)
            if (order["type"] == "buy" and order["price"] > price) or (order["type"] == "sell" and order["price"] < price):
                print(f'Order {order["_id"]} executed, updating status to completed...')
                await complete_limit_order(order["_id"], order["type"])

def run_fetch_stock_price():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(fetch_stock_price())
    finally:
        loop.close()

schedule.every(25).seconds.do(run_fetch_stock_price)

while True:
    schedule.run_pending()
    time.sleep(1)