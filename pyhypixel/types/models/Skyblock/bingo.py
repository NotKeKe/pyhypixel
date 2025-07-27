from pydantic import BaseModel
from typing import List

class BingoEvent(BaseModel):
    key: int
    points: int
    completed_goals: list[str]

class Bingo(BaseModel):
    '''Bingo data for participated events of the provided player.\n`v2/skyblock/bingo'''
    success: bool
    event: List[BingoEvent]