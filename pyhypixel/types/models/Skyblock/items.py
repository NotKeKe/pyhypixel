from pydantic import BaseModel
from typing import List

class Skin(BaseModel):
    value: str
    signature: str

class Item(BaseModel):
    material: str
    durability: int
    skin: Skin
    name: str
    category: str
    tier: str
    npc_sell_price: int
    id: str

class Items(BaseModel):
    '''Information regarding items in the SkyBlock game.\n`v2/resources/skyblock/items`'''
    success: bool
    lastUpdated: int
    items: List[Item]