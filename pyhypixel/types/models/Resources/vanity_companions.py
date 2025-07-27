from pydantic import BaseModel
from typing import List, Union, Any

class Types(BaseModel):
    key: str
    name: str
    rarity: Union[str, Any]
    package: str

class VanityCompanions(BaseModel):
    success: bool
    lastUpdated: int
    types: List[Types]