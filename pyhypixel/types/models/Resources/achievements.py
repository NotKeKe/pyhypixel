from pydantic import BaseModel
from typing import Optional, Dict, List

class OneTimeAchievement(BaseModel):
    points: int
    name: str
    description: str
    gamePercentUnlocked: Optional[float] = None
    globalPercentUnlocked: Optional[float] = None
    legacy: Optional[bool] = None
    secret: Optional[bool] = None

class Tier(BaseModel):
    tier: int
    points: int
    amount: int

class TieredAchievement(BaseModel):
    name: str
    description: str
    tiers: List[Tier]
    legacy: Optional[bool] = None

class GameAchievements(BaseModel):
    one_time: Dict[str, OneTimeAchievement]
    tiered: Dict[str, TieredAchievement]
    total_points: int
    total_legacy_points: int

class Achievements(BaseModel):
    '''`v2/resources/achievements`'''
    success: bool
    lastUpdated: int
    achievements: Dict[str, GameAchievements]