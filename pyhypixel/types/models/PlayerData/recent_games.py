from pydantic import BaseModel
from typing import List

class Games(BaseModel):
    data: int
    gameType: str
    mode: str
    map: str
    ended: int

class RecentGames(BaseModel):
    '''The recently played games of a specific player\n`v2/recentgames`'''
    success: bool
    uuid: str
    games: List[Games]