from pydantic import BaseModel, TypeAdapter
from typing import List

class Cookies(BaseModel):
    current: int

class House(BaseModel):
    uuid: str
    owner: str
    name: str
    createdAt: int
    players: int
    cookies: Cookies

Houses = TypeAdapter(List[House])