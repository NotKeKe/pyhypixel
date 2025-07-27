from pydantic import BaseModel
from typing import List, Dict, Optional

class Rewards(BaseModel):
    type: str
    amount: int

class Objectives(BaseModel):
    id: str
    type: str
    integer: Optional[int] = None

class Requirements(BaseModel):
    type: str

class Quest(BaseModel):
    id: str
    name: str
    rewards: List[Rewards]
    objectives: List[Objectives]
    requirements: List[Requirements]
    description: str

class Quests(BaseModel):
    '''`v2/resources/quests`'''
    success: bool
    quests: Dict[str, List[Quest]]