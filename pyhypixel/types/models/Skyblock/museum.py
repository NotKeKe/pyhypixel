from pydantic import BaseModel
from typing import Dict, Optional, Any, List

class Item(BaseModel):
    type: int
    data: str 

class ItemName(BaseModel):
    donated_time: int
    featured_slot: Optional[str] = None
    items: Item

class MuseumItem(BaseModel):
    value: int
    appraisal: bool
    items: Dict[str, ItemName]
    special: Optional[List[ItemName]] = None

class Museum(BaseModel):
    '''SkyBlock museum data for all members of the provided profile. The data returned can differ depending on the players in-game API settings.\n`v2/skyblock/museum`'''
    success: bool
    members: Optional[Dict[str, MuseumItem]] = None
    profile: Optional[MuseumItem] = None
    