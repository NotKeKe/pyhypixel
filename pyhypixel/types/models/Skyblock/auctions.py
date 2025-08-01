from pydantic import BaseModel
from typing import List

class Bid(BaseModel):
    """
    代表一次競標的紀錄。
    """
    auction_id: str
    bidder: str
    profile_id: str
    amount: int
    timestamp: int

class Auction(BaseModel):
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
    item_bytes: str
    claimed: bool
    claimed_bidders: List[str]
    highest_bid_amount: int
    bids: List[Bid]

class Auctions(BaseModel):
    '''Returns the currently active auctions sorted by last updated first and paginated.\n`v2/skyblock/auctions`'''
    success: bool
    page: int
    totalPages: int
    totalAuctions: int
    lastUpdated: int
    auctions: List[Auction]
