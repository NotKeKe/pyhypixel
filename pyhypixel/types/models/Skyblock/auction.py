from pydantic import BaseModel
from typing import List

class ItemBytes(BaseModel):
    """
    代表物品的二進位資料結構。
    """
    type: int
    data: str

class Bid(BaseModel):
    """
    代表一次競標的紀錄。
    """
    auction_id: str
    bidder: str
    profile_id: str
    amount: int
    timestamp: int

class Item(BaseModel):
    """
    代表一個拍賣品的所有資訊。
    """
    uuid: str
    auctioneer: str
    profile_id: str
    coop: List[str]
    start: int
    end: int
    item_name: str
    item_lore: str
    extra: str
    category: str
    tier: str
    starting_bid: int
    item_bytes: ItemBytes
    claimed: bool
    claimed_bidders: List[str]
    highest_bid_amount: int
    bids: List[Bid]

class Auction(BaseModel):
    '''Returns the auctions selected by the provided query. Only one query parameter can be used in a single request, and cannot be filtered by multiple.\n`v2/skyblock/auction`'''
    success: bool
    auctions: List[Item]