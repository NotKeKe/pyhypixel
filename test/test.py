import requests
import json

KEY = '29906ec8-cfc9-4ab9-a492-734cbf8faaed'
UUID = '552e9105aa1f47d2ba3f473b0b1d7292' # me
UUID2 = 'f9922e748cce48288bcc5a74b4c0178a' # dulin
UUID3 = 'e9ea9e01fe1c436788a8c437b459012a' # redmoon
base_url = 'https://api.hypixel.net/'

headers = {
    'API-Key': KEY
}

params = {
    'player': UUID2
}

def req():
    resp = requests.get(f'{base_url}v2/resources/vanity/companions', 
                        headers=headers,
                        # params=params
                    )
    with open('./test/test.json', mode='w', encoding='utf-8') as f:
        json.dump(resp.json(), f, ensure_ascii=False, indent=4)

def main():
    from pyhypixel.hypixel_api import HypixelApi
    import asyncio

    hyp = HypixelApi(KEY)

    async def main():
        a = await hyp.Resources.vanity_champanions()
        print('')

    asyncio.run(main())

# req()
main()