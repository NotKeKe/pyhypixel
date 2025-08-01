from aiohttp import ClientResponse
from yarl import URL

from .req.player_data import PlayerData
from .req.resources import Resources
from .req.skyblock import Skyblock
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
        self.Resources = Resources(self)
        self.Skyblock = Skyblock(self)

    def get_rate(self, resp: ClientResponse) -> None:
        rate_limit = resp.headers.get('ratelimit-limit')
        rate_remain = resp.headers.get('ratelimit-remaining')
        rate_reset = resp.headers.get('ratelimit-reset')

        if rate_limit is not None:
            self.rate_limit = int(resp.headers.get('ratelimit-limit'))
        if rate_remain is not None:
            self.rate_remain = int(resp.headers.get('ratelimit-remaining'))
        if rate_reset is not None:
            self.rate_reset = int(resp.headers.get('ratelimit-reset'))