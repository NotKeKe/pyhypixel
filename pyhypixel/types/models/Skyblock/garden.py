from pydantic import BaseModel
from typing import Dict, Optional, List

# composter_data
class Upgrade(BaseModel):
    speed: int
    multi_drop: int
    fuel_cap: int
    organic_matter_cap: int
    cost_reduction: int

class ComposterData(BaseModel):
    organic_matter: float
    fuel_units: float
    compost_units: int
    compost_items: int
    conversion_ticks: int
    last_save: int
    upgrades: Optional[Upgrade]

# active_commissions
class Requirement(BaseModel):
    original_item: str
    original_amount: int
    item: str
    amount: int

class ActiveCommission(BaseModel):
    requirement: List[Requirement]
    status: str
    position: int

class Garden(BaseModel):
    '''SkyBlock garden data for the provided profile.\n`v2/skyblock/garden``'''
    success: bool
    uuid: str
    active_commissions: Dict[str, ActiveCommission]
    commission_data: Dict[str, Dict[str, int]]
    composter_data: ComposterData
    resources_collected: Dict[str, int]
    crop_upgrade_levels: Dict[str, int]
    garden_experience: float
    unlocked_plots_ids: List[str]
    unlocked_barn_skins: List[str]
    selected_barn_skin: str