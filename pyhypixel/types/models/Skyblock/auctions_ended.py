from pydantic import BaseModel
from typing import List

class Auction(BaseModel):
    auction_id: str
    seller: str
    seller_profile: str
    buyer: str
    buyer_profile: str
    timestamp: int
    price: int
    bin: bool
    item_bytes: str

class AuctionsEnded(BaseModel):
    '''SkyBlock auctions which ended in the last 60 seconds.\n`v2/skyblock/auctions_ended'''
    success: bool
    lastUpdated: int
    auctions: List[Auction]