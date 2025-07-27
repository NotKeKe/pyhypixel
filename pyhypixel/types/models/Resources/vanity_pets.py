from pydantic import BaseModel
from typing import Any

class VanityPets(BaseModel):
    '''`v2/resources/vanity/pets`'''
    success: bool
    lastUpdated: int
    types: Any
    rarities: Any