from aiohttp import ClientSession, ClientResponse

from types.err.error import req_error

class Skyblock:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = 'https://api.hypixel.net/'

        # for request
        self.header = {
            'API-Key': self.api_key
        }

        # for rate limit
        self.rate_limit = None # limit of requests per min
        self.rate_remain = None # 該分鐘 剩餘的請求次數
        self.rate_reset = None # seconds untils next min for reset

    def get_rate(self, resp: ClientResponse) -> None:
        self.rate_limit = int(resp.headers.get('X-RateLimit-Limit'))
        self.rate_remain = int(resp.headers.get('X-RateLimit-Remaining'))
        self.rate_reset = int(resp.headers.get('X-RateLimit-Reset'))

    async def get_player_data(self, uuid: str) -> dict:
        async with ClientSession() as session:
            async with session.get(f'{self.base_url}v2/player', headers=self.header, params={'uuid': uuid}) as resp:
                req_error(resp)
                self.get_rate(resp)
                
                return await resp.json()