from pydantic import BaseModel
from typing import List, Optional

class Event(BaseModel):
    key: int
    points: int
    completed_goals: List[str]

class Bingo(BaseModel):
    '''Bingo data for participated events of the provided player.\n`v2/skyblock/bingo'''
    success: bool
    events: List[Event]