from pydantic import BaseModel

class Cookies(BaseModel):
    current: int

class House(BaseModel):
    '''Information about a specific house.\n`v2/housing/house`'''
    success: bool
    uuid: str
    owner: str
    name: str
    createdAt: int
    players: int
    cookies: Cookies