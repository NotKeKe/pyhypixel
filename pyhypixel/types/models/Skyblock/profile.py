from typing import List, Dict, Any
from pydantic import BaseModel

class DeletionNotice(BaseModel):
    timestamp: int

class MemberProfileInfo(BaseModel):
    deletion_notice: DeletionNotice

class MembersInfo(BaseModel):
    player_id: str
    profile: MemberProfileInfo

class Transaction(BaseModel):
    timestamp: int
    action: str
    initiator_name: str
    amount: int

class Banking(BaseModel):
    balance: int
    transactions: List[Transaction]

class profile(BaseModel):
    profile_id: str
    members: MembersInfo
    cute_name: str
    selected: bool
    community_upgrades: Dict[str, Any]
    banking: Banking
    game_mode: str

class Profile(BaseModel):
    '''SkyBlock profile data, such as stats, objectives etc. The data returned can differ depending on the players in-game API settings.\n`v2/skyblock/profile`'''
    success: bool
    profile: profile