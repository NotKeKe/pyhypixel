from typing import TYPE_CHECKING, Union, Optional, Dict
from aiohttp import ClientResponse

from ..interfaces.api import API
from ..types.models.Skyblock import *
from ..types.models.error import ErrorResponse
from ..utils import get, model_validate

if TYPE_CHECKING:
    from hypixel_api import HypixelApi

class Skyblock:
    def __init__(self, HypixelAPI: 'HypixelApi'):
        self.HypixelAPI = HypixelAPI

        self.api_key = HypixelAPI.api_key
        self.base_url = HypixelAPI.base_url

        # for request
        self.headers = HypixelAPI.headers

    def get_rate(self, resp: ClientResponse):
        self.HypixelAPI.get_rate(resp)

    async def collections(self) -> Union[Collections, ErrorResponse]:
        """Information regarding Collections in the SkyBlock game.

        Returns:
            Union[Collections, ErrorResponse]
        """        
        data = await get(self, self.base_url.with_path('v2/resources/skyblock/collections'))
        return Collections.model_validate(data) if data.get('success') else ErrorResponse.model_validate(data)
    
    async def skills(self) -> Union[Skills, ErrorResponse]:
        """Information regarding Skills in the SkyBlock game.

        Returns:
            Union[Skills, ErrorResponse]
        """        
        data = await get(self, self.base_url.with_path('v2/resources/skyblock/skills'))
        return Skills.model_validate(data) if data.get('success') else ErrorResponse.model_validate(data)
    
    async def items(self) -> Union[Items, ErrorResponse]:
        """Information regarding items in the SkyBlock game.

        Returns:
            Union[Items, ErrorResponse]
        """
        data = await get(self, self.base_url.with_path('v2/resources/skyblock/items'))
        return Items.model_validate(data) if data.get('success') else ErrorResponse.model_validate(data)
    
    async def election_and_mayor(self) -> Union[ElectionAndMayor, ErrorResponse]:
        """Information regarding the current mayor and ongoing election in SkyBlock.

        Returns:
            Union[ElectionAndMayor, ErrorResponse]
        """
        data = await get(self, self.base_url.with_path('v2/resources/skyblock/election'))
        return ElectionAndMayor.model_validate(data) if data.get('success') else ErrorResponse.model_validate(data)

    async def bingo_data(self) -> Union[ResourceBingo, ErrorResponse]:
        '''Information regarding the current ResourceBingo event and its goals.. 

        Returns:
            Union[ResourceBingo, ErrorResponse]
        '''
        data = await get(self, self.base_url.with_path('v2/resources/skyblock/bingo'))
        return ResourceBingo.model_validate(data) if data.get('success') else ErrorResponse.model_validate(data)
    
    async def news(self) -> Union[News, ErrorResponse]:
        """News

        Returns:
            Union[News, ErrorResponse]
        """        
        data = await get(self, self.base_url.with_path('v2/skyblock/news'))
        return model_validate(News, data)
    
    async def auction(self, auction_uuid: Optional[str] = None, player_uuid: Optional[str] = None, profile_uuid: Optional[str] = None) -> Union[Auction, ErrorResponse]:
        """Returns the auctions selected by the provided query. Only one query parameter can be used in a single request, and cannot be filtered by multiple.

        Args:
            auction_uuid (Optional[str], optional): _description_. Defaults to None.
            player_uuid (Optional[str], optional): _description_. Defaults to None.
            profile_uuid (Optional[str], optional): _description_. Defaults to None.

        Returns:
            Union[Auction, ErrorResponse]
        """        
        args = {'uuid': auction_uuid, 'player': player_uuid, 'profile': profile_uuid}
        params = {k: v for k, v in args.items() if v is not None}
        data = await get(self, self.base_url.with_path('v2/skyblock/auction'), params)
        return model_validate(Auction, data)
    
    async def auctions(self, page: Optional[int] = 0) -> Union[Auctions, ErrorResponse]:
        """Returns the currently active auctions sorted by last updated first and paginated.

        Args:
            page (Optional[int], optional): _description_. Defaults to 0.

        Returns:
            Union[Auctions, ErrorResponse]
        """        
        params = {'page': page}
        data = await get(self, self.base_url.with_path('v2/skyblock/auctions'), params)
        return model_validate(Auctions, data)

    async def auctions_ended(self) -> Union[AuctionsEnded, ErrorResponse]:
        """SkyBlock auctions which ended in the last 60 seconds.

        Returns:
            Union[AuctionsEnded, ErrorResponse]
        """        
        data = await get(self, self.base_url.with_path('v2/skyblock/auctions_ended'))
        return model_validate(AuctionsEnded, data)
    
    async def bazaar(self) -> Union[Bazaar, ErrorResponse]:
        """Returns the list of products along with their sell summary, buy summary and quick status.

        Returns:
            Union[Bazaar, ErrorResponse]: _description_
        """        
        data = await get(self, self.base_url.with_path('v2/skyblock/bazaar'))
        return model_validate(Bazaar, data)
    
    async def profile(self, profile_uuid: str) -> Union[Profile, ErrorResponse]:
        """Get profile extra data by `profile uuid`
        SkyBlock profile data, such as stats, objectives etc. The data returned can differ depending on the players in-game API settings.

        Returns:
            Union[Profile, ErrorResponse]
        """        
        params = {'profile': profile_uuid}
        data = await get(self, self.base_url.with_path('v2/skyblock/profile'), params)
        return model_validate(Profile, data)
    
    async def profiles(self, player_uuid: str) -> Union[Profiles, ErrorResponse]:
        """Get profiles by `player uuid`
        By me: (It's too difficult to find the patterns of the API responses; the official website is also wrong, so we can't use IntelliSense.)

        Returns:
            Union[Profiles, ErrorResponse]: _description_
        """        
        params = {'uuid': player_uuid}
        data = await get(self, self.base_url.with_path('v2/skyblock/profiles'), params)
        return model_validate(Profiles, data)
    
    async def museum(self, player_uuid: str) -> Union[Museum, ErrorResponse]:
        """SkyBlock museum data for all members of the provided player. The data returned can differ depending on the players in-game API settings.

        Args:
            player_uuid (str)

        Returns:
            Union[Museum, ErrorResponse]
        """        
        params = {'profile': player_uuid}
        data = await get(self, self.base_url.with_path('v2/skyblock/museum'), params)
        return model_validate(Museum, data)
    
    async def garden(self, player_uuid: str) -> Union[Garden, ErrorResponse]:
        """SkyBlock garden data for the provided profile.

        Args:
            player_uuid (str)

        Returns:
            Union[Garden, ErrorResponse]
        """        
        params = {'profile': player_uuid}
        data = await get(self, self.base_url.with_path('v2/skyblock/garden'), params)
        return model_validate(Garden, data)
    
    async def bingo_player(self, player_uuid: str) -> Union[Bingo, ErrorResponse]:
        """SkyBlock bingo data for the provided player.

        Args:
            player_uuid (str)

        Returns:
            Union[Bingo, ErrorResponse]
        """
        params = {'uuid': player_uuid}
        data = await get(self, self.base_url.with_path('v2/skyblock/bingo'), params)
        return model_validate(Bingo, data)
    
    async def firesales(self) -> Union[Firesales, ErrorResponse]:
        """Retrieve the currently active or upcoming Fire Sales for SkyBlock.

        Args:
            player_uuid (str)

        Returns:
            Union[Firesales, ErrorResponse]
        """
        data = await get(self, self.base_url.with_path('v2/skyblock/firesales'))
        return model_validate(Firesales, data)