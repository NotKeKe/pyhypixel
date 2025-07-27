from pydantic import BaseModel
from typing import Any

class VanityCompanions(BaseModel):
    success: bool
    lastUpdated: int
    types: Any