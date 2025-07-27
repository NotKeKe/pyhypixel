from pydantic import BaseModel, Field
from typing import Dict, List

class Tier(BaseModel):
    """
    代表單一階級的解鎖條件與獎勵。
    """
    tier: int
    amount_required: int = Field(..., alias='amountRequired')
    unlocks: List[str]

class Item(BaseModel):
    """
    代表一個可收集的物品及其所有階級資訊。
    """
    name: str
    max_tiers: int = Field(..., alias='maxTiers')
    tiers: List[Tier]

class Collection(BaseModel):
    """
    代表一個物品收藏類別，例如「農耕」或「採礦」。
    """
    name: str
    items: Dict[str, Item]

class Collections(BaseModel):
    '''Information regarding Collections in the SkyBlock game.\n`v2/resources/skyblock/collections`'''
    success: bool
    lastUpdated: int
    version: str
    collections: Dict[str, Collection]