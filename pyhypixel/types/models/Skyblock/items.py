from pydantic import BaseModel
from typing import List, Optional, Dict, Union, Any

class Skin(BaseModel):
    value: str
    signature: Optional[str] = None

class CataRequirements(BaseModel):
    type: str
    dungeon_type: str
    level: int

class GemstoneSlotsCosts(BaseModel):
    slot_type: Optional[str] = None
    type: Optional[str] = None
    item_id: Optional[str] = None
    amount: Optional[int] = None
    coins: Optional[int] = None

class GemstoneSlots(BaseModel):
    slot_type: str
    costs: Optional[List[GemstoneSlotsCosts]] = None

class MuseumData(BaseModel):
    donation_xp: Optional[int] = None
    type: str
    parent: Optional[Dict[str, str]] = None

class DungeonItemConversionCost(BaseModel):
    essence_type: str
    amount: int

class PrestigeCosts(BaseModel):
    type: str
    essence_type: Optional[str] = None
    amount: int
    item_id: Optional[str] = None

class Prestige(BaseModel):
    item_id: str
    cost: Optional[List[PrestigeCosts]] = None

class UpgradeCosts(BaseModel):
    type: str
    essence_type: Optional[str] = None
    amount: int

class Item(BaseModel):
    material: str
    durability: Optional[int] = None
    skin: Optional[Skin] = None
    name: str
    category: Optional[str] = None
    tier: Optional[str] = None
    npc_sell_price: Optional[float] = None
    id: str
    color: Optional[str] = None
    upgrade_costs: Optional[List[List[UpgradeCosts]]] = None
    museum_data: Optional[MuseumData] = None
    stats: Optional[Dict[str, float]] = None
    dungeon_item_conversion_cost: Optional[DungeonItemConversionCost] = None
    catacombs_requirements: Optional[List[CataRequirements]] = None
    gemstone_slots: Optional[List[GemstoneSlots]] = None
    prestige: Optional[Prestige] = None
    requirements: Optional[List[Dict[str, Union[str, Union[int, List[Dict[str, Union[int, str]]]]]]]] = None
    item_specific: Optional[Any] = None

class Items(BaseModel):
    '''Information regarding items in the SkyBlock game.\n`v2/resources/skyblock/items`'''
    success: bool
    lastUpdated: int
    items: List[Item]