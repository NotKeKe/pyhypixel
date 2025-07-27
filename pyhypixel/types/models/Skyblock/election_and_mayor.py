from pydantic import BaseModel
from typing import List, Dict, Optional

class Perk(BaseModel):
    name: str
    description: str
    minister: Optional[bool]

class Candidates(BaseModel):
    key: str
    name: str
    perks: List[Perk]
    votes: int

class Election(BaseModel):
    year: int
    candidates: List[Candidates]

class Mayor(BaseModel):
    key: str
    name: str
    perks: List[Perk]
    election: Election

class Current(BaseModel):
    year: int
    candidates: List[Candidates]

class ElectionAndMayor(BaseModel):
    '''Information regarding the current mayor and ongoing election in SkyBlock.\n`v2/resources/skyblock/election`'''
    success: bool
    lastUpdated: int
    mayor: Mayor
    current: Current