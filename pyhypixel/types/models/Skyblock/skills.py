from pydantic import BaseModel, Field
from typing import Dict, List

class SkillLevel(BaseModel):
    """
    代表單一技能等級的詳細資訊，包括所需經驗和解鎖的獎勵。
    """
    level: int
    total_exp_required: float = Field(..., alias='totalExpRequired')
    unlocks: List[str]

class Skill(BaseModel):
    """
    代表一個完整的技能類別，例如「農耕」或「採礦」，包含其所有等級資訊。
    """
    name: str
    description: str
    max_level: int = Field(..., alias='maxLevel')
    levels: List[SkillLevel]

class Skills(BaseModel):
    '''Information regarding skills in the SkyBlock game.\n`v2/resources/skyblock/skills`'''
    success: bool
    lastUpdated: int
    version: str
    skills: Dict[str, Skill]