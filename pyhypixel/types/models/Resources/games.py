from pydantic import BaseModel
from typing import Dict, Optional

class Game(BaseModel):
    id: int
    name: str
    databaseName: str
    modeNames: Optional[Dict[str, str]]

    model_config = {
        "extra": "allow"
    }

class Games(BaseModel):
    '''Returns information about Hypixel Games.\n`v2/resources/games`'''
    success: bool
    lastUpdated: int
    games: Dict[str, Game]