from aiohttp import ClientSession
from typing import Union, List, Dict

from ..types.err.error import req_error

async def get(cls, url: str, params: dict) -> Union[Dict, List]:
    async with ClientSession() as session:
        async with session.get(url, params=params, headers=cls.headers) as resp:
            req_error(resp)
            cls.get_rate(resp)

            return await resp.json()