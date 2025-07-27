from pydantic import BaseModel
from typing import Dict, List

class Reward(BaseModel):
    type: str
    amount: int

class Challenge(BaseModel):
    id: str
    name: str
    rewards: List[Reward]

class Challenges(BaseModel):
    '''`v2/resources/challenges`'''
    success: bool
    lastUpdated: int
    challenges: Dict[str, List[Challenge]]