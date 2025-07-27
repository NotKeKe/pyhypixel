from pydantic import BaseModel
from typing import Any

class Challenges(BaseModel):
    '''`v2/resources/challenges`'''
    success: bool
    lastUpdated: int
    challenges: Any