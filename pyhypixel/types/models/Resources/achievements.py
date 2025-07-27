from pydantic import BaseModel
from typing import Any

class Achievements(BaseModel):
    '''`v2/resources/achievements`'''
    success: bool
    lastUpdated: int
    achievements: Any