from pydantic import BaseModel
from typing import Dict, Optional, List, Union

# composter_data
class Upgrade(BaseModel):
    speed: int
    multi_drop: int
    fuel_cap: int
    organic_matter_cap: int
    cost_reduction: Optional[int] = None

class ComposterData(BaseModel):
    organic_matter: float
    fuel_units: float
    compost_units: int
    compost_items: int
    conversion_ticks: int
    last_save: int
    upgrades: Optional[Union[Upgrade, Dict]] = None

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

class GardenData(BaseModel):
    uuid: str
    unlocked_plots_ids: List[str]
    commission_data: Dict[str, Union[Dict[str, int], int]]
    resources_collected: Dict[str, int]
    composter_data: ComposterData
    active_commissions: Dict[str, ActiveCommission]
    garden_experience: float
    crop_upgrade_levels: Dict[str, int]
    unlocked_barn_skins: List[str]
    selected_barn_skin: str

class Garden(BaseModel):
    '''SkyBlock garden data for the provided profile.\n`v2/skyblock/garden``'''
    success: bool
    garden: GardenData