from pydantic import BaseModel
from typing import Dict, Optional

class Game(BaseModel):
    player: int
    modes: Optional[Dict[str, int]]

class Counts(BaseModel):
    '''Current Player Counts\n`v2/counts`'''
    success: bool
    playerCount: int
    games: Dict[str, Game]