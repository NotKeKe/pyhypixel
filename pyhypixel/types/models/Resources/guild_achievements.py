from pydantic import BaseModel
from typing import Dict, List

class Tiers(BaseModel):
    tier: int
    amount: int

class Introduction(BaseModel):
    name: str
    description: str
    tiers: List[Tiers]

class Tiered(BaseModel):
    PRESTIGE: Introduction
    EXPERIENCE_KINGS: Introduction
    WINNERS: Introduction
    ONLINE_PLAYERS: Introduction

class GuildAchievements(BaseModel):
    '''`v2/resources/guild/achievements`'''
    success: bool
    lastUpdated: int
    one_time: Dict
    tiered: Tiered