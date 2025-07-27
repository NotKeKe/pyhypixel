from pydantic import BaseModel
from typing import List, Optional

class Types(BaseModel):
    key: str
    name: str
    rarity: Optional[str]
    package: str

class Rarities(BaseModel):
    name: str
    color: str

class VanityPets(BaseModel):
    '''`v2/resources/vanity/pets`'''
    success: bool
    lastUpdated: int
    types: List[Types]
    rarities: List[Rarities]