# 股票交易自動化系統

這是一個使用 Python、MongoDB 和其他工具實現的股票交易自動化系統。

## 目錄

- [股票交易自動化系統](#股票交易自動化系統)
  - [目錄](#目錄)
  - [安裝](#安裝)
  - [使用方法](#使用方法)
  - [功能](#功能)
  - [貢獻](#貢獻)
  - [授權](#授權)

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

## 貢獻

如果您想為這個專案作出貢獻，請閱讀 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 授權

該專案使用 ISC 授權，詳情請查看 [LICENSE.md](LICENSE.md)。
