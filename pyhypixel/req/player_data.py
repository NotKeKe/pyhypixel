from typing import TYPE_CHECKING, Union, Optional, Dict
from aiohttp import ClientResponse

from ..interfaces.api import API
from ..types.models.PlayerData import *
from ..types.models.error import ErrorResponse
from ..utils import get

if TYPE_CHECKING:
    from hypixel_api import HypixelApi

class PlayerData(API):
    def __init__(self, HypixelAPI: 'HypixelApi'):
        self.HypixelAPI = HypixelAPI

        self.api_key = HypixelAPI.api_key
        self.base_url = HypixelAPI.base_url

        # for request
        self.headers = HypixelAPI.headers

    def get_rate(self, resp: ClientResponse):
        self.HypixelAPI.get_rate(resp)

    async def get_data(self, uuid: str) -> Union[Player, ErrorResponse]:
        """Data of a specific player, including game stats

        Args:
            uuid (str): user's uuid

        Returns:
            Union[Player, ErrorResponse]
        """        
        data = await get(self, self.base_url.with_path('/v2/player'), params={'uuid': uuid})
        return Player.model_validate(data) if data.get('success') else ErrorResponse.model_validate(data)

    async def recent_games(self, uuid: str) -> Union[RecentGames, ErrorResponse]:
        """The recently played games of a specific player

        Args:
            uuid (str): user's uuid

        Returns:
            Union[RecentGames, ErrorResponse]
        """        
        data = await get(self, self.base_url.with_path('/v2/recentgames'), params={'uuid': uuid})
        return RecentGames.model_validate(data) if data.get('success') else ErrorResponse.model_validate(data)
        
    async def status(self, uuid: str) -> Union[Status, ErrorResponse]:
        """The current online status of a specific player

        Args:
            uuid (str): user's uuid

        Returns:
            Union[Status, ErrorResponse]
        """        
        data = await get(self, self.base_url.with_path('/v2/status'), params={'uuid': uuid})
        return Status.model_validate(data) if data.get('success') else ErrorResponse.model_validate(data)
    
    async def guild(self, id: Optional[str] = None, uuid: Optional[str] = None, name: Optional[str] = None) -> Union[Guild, ErrorResponse]:
        """Retrieve a Guild by a player, id, or name (choose one)

        Args:
            id (str): i don't know what it is.
            uuid (str): player's uuid
            name (str): user's name

        Returns:
            Union[Guild, ErrorResponse]
        """        
        if id is None and uuid is None and name is None:
            raise ValueError('Please provide one variable')
        
        data = await get(self, self.base_url.with_path('/v2/guild'), 
                            params={
                                **({'id': id} if id is not None else {}), 
                                **({'player': uuid} if uuid is not None else {}), 
                                **({'name': name} if name is not None else {})
                            }
                        )
        return Guild.model_validate(data) if data.get('success') else ErrorResponse.model_validate(data)
    
