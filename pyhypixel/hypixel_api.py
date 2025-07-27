from aiohttp import ClientResponse
from yarl import URL

from .req.player_data import PlayerData
from .interfaces.api import API

class HypixelApi(API):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = URL('https://api.hypixel.net')

        # for request
        self.headers = {
            'API-Key': self.api_key
        }

        # for rate limit
        self.rate_limit = None # limit of requests per min
        self.rate_remain = None # 該分鐘 剩餘的請求次數
        self.rate_reset = None # seconds untils next min for reset

        self.PlayerData = PlayerData(self)

    def get_rate(self, resp: ClientResponse) -> None:
        self.rate_limit = int(resp.headers.get('ratelimit-limit'))
        self.rate_remain = int(resp.headers.get('ratelimit-remaining'))
        self.rate_reset = int(resp.headers.get('ratelimit-reset'))