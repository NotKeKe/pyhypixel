from pydantic import BaseModel
from typing import List, Optional

class Goal(BaseModel):
    id: str
    name: str
    tiers: Optional[List[int]]
    progress: Optional[int]
    lore: str
    fullLore: List[str]
    requiredAmount: Optional[int]

class ResourceBingo(BaseModel):
    '''Information regarding the current bingo event and its goals.\n`v2/resources/skyblock/bingo`'''
    success: bool
    lastUpdated: int
    id: int
    name: str
    start: int
    end: int
    modifier: str
    goals: List[Goal]