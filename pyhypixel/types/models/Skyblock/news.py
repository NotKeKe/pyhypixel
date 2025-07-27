from pydantic import BaseModel
from typing import List

class ItemOfItem(BaseModel):
    material: str

class Item(BaseModel):
    item: ItemOfItem
    link: str
    text: str
    title: str

class News(BaseModel):
    '''`v2/skyblock/news`, api required'''
    success: bool
    items: List[Item]