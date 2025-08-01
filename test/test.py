import requests
import json
from pprint import pp

import os
from dotenv import load_dotenv
load_dotenv()

KEY = os.getenv('KEY')
UUID = '552e9105aa1f47d2ba3f473b0b1d7292' # me
UUID2 = 'f9922e748cce48288bcc5a74b4c0178a' # dulin
UUID3 = 'e9ea9e01fe1c436788a8c437b459012a' # redmoon
UUID4 = '90d664d89fd44d8f8a393a9084299503' # yy
PROFILE_UUID = '45946595-68c5-435f-8404-ee014857b908' # me
PROFILE_UUID2 = '45946595-68c5-435f-8404-ee014857b908' # yy
base_url = 'https://api.hypixel.net/'

headers = {
    'API-Key': KEY
}

params = {
    'uuid': UUID
}

def req():
    resp = requests.get(f'{base_url}v2/skyblock/bingo', 
                        headers=headers,
                        params=params
                    )
    with open('./test/test.json', mode='w', encoding='utf-8') as f:
        json.dump(resp.json(), f, ensure_ascii=False, indent=4)

def main():
    from pyhypixel.hypixel_api import HypixelApi
    import asyncio

    hyp = HypixelApi(KEY)

    async def main():
        a = await hyp.Skyblock.firesales()
        pp('')

    asyncio.run(main())

# req()
main()