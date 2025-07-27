# 仍在開發中 (Still developing) (20250727)

## 簡介
**! 此專案並非由 hypixel 官方開發 !**
該專案主要使用 aiohttp 來做高效的異步 (async) 請求，以及使用 pydantic 來轉換數據。
HypixelApi 底下的路徑完全按照 [api.hypixel.net](https://api.hypixel.net/) 的連結路徑來製作，所以如果有任何不清楚的可以直接去官網看看。

## Done
[x] PlayerData 的指令

## Quick Start
1. 安裝
2. 
    ```python
    # 導入庫
    from {庫的名字，目前為pyhypixel}.hypixel_api import HypixelApi

    # 創建一個 HypixelApi 物件
    hyp = HypixelApi(api_key = 'YOUR_API_KEY_HERE')

    # 查詢使用者在線狀態
    status = hyp.PlayerData.status()
    print(status.session.online)
    ```