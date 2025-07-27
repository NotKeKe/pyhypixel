from pydantic import BaseModel
from typing import Union, List, Dict, Optional

class Member(BaseModel):
    uuid: str
    rank: str
    joined: int
    questParticipation: Optional[int] = None
    mutedTill: Optional[int] = None
    expHistory: Dict[str, int]

class Rank(BaseModel):
    name: str
    default: bool
    tag: Optional[str] = None
    created: int
    priority: int

class GuildData(BaseModel):
    _id: str
    name: str
    name_lower: str
    coins: Union[int, float]
    coinsEver: Union[int, float]
    created: int
    members: List[Member]
    ranks: List[Rank]
    achievements: Dict[str, int]
    exp: int
    tag: str
    publiclyListed: bool
    tagColor: str
    description: Optional[str] = None
    preferredGames: List[str]
    chatMute: Optional[int] = None
    guildExpByGameType: Dict[str, int]

class Guild(BaseModel):
    '''Retrieve a Guild by a player, id, or name\nv2/guild'''
    success: bool
    guild: Optional[GuildData] = None