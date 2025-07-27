from typing import List, Dict
from pydantic import BaseModel

class SummaryItem(BaseModel):
    amount: int
    pricePerUnit: float
    orders: int

class QuickStatus(BaseModel):
    productId: str
    sellPrice: float
    sellVolume: int
    sellMovingWeek: int
    sellOrders: int
    buyPrice: float
    buyVolume: int
    buyMovingWeek: int
    buyOrders: int

class Product(BaseModel):
    product_id: str
    sell_summary: List[SummaryItem]
    buy_summary: List[SummaryItem]
    quick_status: QuickStatus

class Bazaar(BaseModel):
    success: bool
    lastUpdated: int
    products: Dict[str, Product]