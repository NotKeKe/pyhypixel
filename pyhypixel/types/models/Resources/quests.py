from pydantic import BaseModel
from typing import Any

class Quests(BaseModel):
    '''`v2/resources/quests`'''
    success: bool
    quests: Any