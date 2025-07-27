from pydantic import BaseModel
from typing import List

class Sale(BaseModel):
    item_id: str
    start: int
    end: int
    amount: int
    price: int

class Firesales(BaseModel):
    '''Retrieve the currently active or upcoming Fire Sales for SkyBlock.\n`v2/skyblock/firesales`'''
    success: bool
    sales: List[Sale]