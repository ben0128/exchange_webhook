# 股票交易自動化系統

這是一個使用 Python、MongoDB 會自動抓取yahoo finance上的股價資訊，並將mongodb中的訂單取出修改成交狀態的程式。

## 目錄

- [成品 DEMO](https://exchange-frontend-tawny.vercel.app/auth)
- [前端 Github (exchange_frontend)](https://github.com/ben0128/exchange_frontend)
- [後端 Github (exchange_backend)](https://github.com/ben0128/exchange_backend)
- [爬蟲 Github (exchange_webhook)](https://github.com/ben0128/exchange_webhook)
- [爬蟲 GoogleColab](https://colab.research.google.com/drive/17FRMISQP6yoO30lUh37KHygg6OfTRg3k?hl=zh-tw#scrollTo=jHpwx_5cW_SB)

### Download Project

```
git clone https://github.com/ben0128/exchange_webhook.git
```
## 目錄

- [股票交易自動化系統](#股票交易自動化系統)
  - [目錄](#目錄)
    - [Download Project](#download-project)
  - [目錄](#目錄-1)
  - [安裝](#安裝)
  - [使用方法](#使用方法)
  - [功能](#功能)

## 安裝

1. 安裝 MongoDB 和相關 Python 套件：

    ```bash
    pip install pymongo dnspython
    ```

2. 安裝 HTTP 客戶端：

    ```bash
    pip install httpx
    ```

3. 安裝排程工具：

    ```bash
    pip install schedule
    ```

4. 安裝異步 I/O 套件：

    ```bash
    pip install nest_asyncio
    ```

## 使用方法

1. 更新 `mongo_url` 變數以連接到您自己的 MongoDB 集群。

2. 在終端機中運行：

    ```bash
    python your_script_name.py
    ```

## 功能

- 從 Yahoo 股票網站抓取實時股價。
- 使用 MongoDB 作為數據庫來存儲訂單和用戶資訊。
- 使用異步 I/O 和排程來自動執行限價訂單。

