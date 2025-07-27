from pydantic import BaseModel
from typing import Any

class GuildAchievements(BaseModel):
    '''`v2/resources/guild/achievements`'''
    success: bool
    lastUpdated: int
    one_time: Any
    tiered: Any