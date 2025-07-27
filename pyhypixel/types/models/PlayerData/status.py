from pydantic import BaseModel
from typing import Optional

class Session(BaseModel):
    online: bool
    gameType: Optional[str] = None
    mode: Optional[str] = None
    map: Optional[str] = None

class Status(BaseModel):
    success: bool
    uuid: str
    session: Session