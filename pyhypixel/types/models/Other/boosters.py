from pydantic import BaseModel
from typing import List

class BoosterState(BaseModel):
    decrementing: bool

class Booster(BaseModel):
    _id: str
    purchaserUuid: str
    amount: float
    originalLength: int
    length: int
    gameType: int
    dateActivated: int
    stacked: List[str]

class Boosters(BaseModel):
    '''Active Network Boosters\n`v2/boosters`'''
    success: bool
    boosters: List[Booster]
    boosterState: BoosterState