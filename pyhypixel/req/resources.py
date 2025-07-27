from typing import TYPE_CHECKING, Union, Optional, Dict
from aiohttp import ClientResponse

from ..interfaces.api import API
from ..types.models.Resources import *
from ..types.models.error import ErrorResponse
from ..utils import get

if TYPE_CHECKING:
    from hypixel_api import HypixelApi

class Resources(API):
    def __init__(self, HypixelAPI: 'HypixelApi'):
        self.HypixelAPI = HypixelAPI

        self.api_key = HypixelAPI.api_key
        self.base_url = HypixelAPI.base_url

        # for request
        self.headers = HypixelAPI.headers

    def get_rate(self, resp: ClientResponse):
        self.HypixelAPI.get_rate(resp)

    async def games(self) -> Union[Games, ErrorResponse]:
        """Returns information about Hypixel Games.
        api key is not required.

        Returns:
            Union[Games, ErrorResponse]
        """        
        data = await get(self, self.base_url.with_path('v2/resources/games'))
        return Games.model_validate(data) if data.get('success') else ErrorResponse.model_validate(data)
    
    async def achievements(self) -> Union[Achievements, ErrorResponse]:
        """IDK The officials said nothing :(

        Returns:
            Union[Achievements, ErrorResponse]
        """        
        data = await get(self, self.base_url.with_path('v2/resources/achievements'))
        return Achievements.model_validate(data) if data.get('success') else ErrorResponse.model_validate(data)
    
    async def challenges(self) -> Union[Challenges, ErrorResponse]:
        """IDK The officials said nothing :(

        Returns:
            Union[Challenges, ErrorResponse]
        """        
        data = await get(self, self.base_url.with_path('v2/resources/challenges'))
        return Challenges.model_validate(data) if data.get('success') else ErrorResponse.model_validate(data)
    
    async def quests(self) -> Union[Quests, ErrorResponse]:
        """IDK The officials said nothing :(

        Returns:
            Union[Quests, ErrorResponse]
        """
        data = await get(self, self.base_url.with_path('v2/resources/quests'))
        return Quests.model_validate(data) if data.get('success') else ErrorResponse.model_validate(data)
    
    async def guild_achievements(self) -> Union[GuildAchievements, ErrorResponse]:
        """IDK The officials said nothing :(

        Returns:
            Union[GuildAchievements, ErrorResponse]
        """
        data = await get(self, self.base_url.with_path('v2/resources/guilds/achievements'))
        return GuildAchievements.model_validate(data) if data.get('success') else ErrorResponse.model_validate(data)
    
    async def vanity_pets(self) -> Union[VanityPets, ErrorResponse]:
        """IDK The officials said nothing :(

        Returns:
            Union[VanityPets, ErrorResponse]
        """
        data = await get(self, self.base_url.with_path('v2/resources/vanity/pets'))
        return VanityPets.model_validate(data) if data.get('success') else ErrorResponse.model_validate(data)
    
    async def vanity_champanions(self) -> Union[VanityCompanions, ErrorResponse]:
        """IDK The officials said nothing :(

        Returns:
            Union[VanityCompanions, ErrorResponse]
        """        
        data = await get(self, self.base_url.with_path('v2/resources/vanity/companions'))
        return VanityCompanions.model_validate(data) if data.get('success') else ErrorResponse.model_validate(data)