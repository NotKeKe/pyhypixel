from pydantic import BaseModel
from typing import List, Dict, Any

class Profiles(BaseModel):
    success: bool
    profiles: List[Dict[Any, Any]]