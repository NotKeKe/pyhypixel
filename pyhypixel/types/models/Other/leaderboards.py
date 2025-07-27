from pydantic import BaseModel
from typing import Dict, List

class Leaderboard(BaseModel):
    path: str
    prefix: str
    title: str
    location: str
    count: int
    leaders: List[str]

class Leaderboards(BaseModel):
    '''Current Leaderboards\n`v2/leaderboards`'''
    success: bool
    leaderboards: Dict[str, List[Leaderboard]]