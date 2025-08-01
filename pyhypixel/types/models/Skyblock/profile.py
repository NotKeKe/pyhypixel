from pydantic import BaseModel
from typing import List, Dict, Any

class PlayerData(BaseModel):
    visited_zones: List[str]
    last_death: int
    active_effects: List[Any]
    visited_modes: List[str]
    unlocked_coll_tiers: List[str]

class EasterRabbits(BaseModel):
    collected_locations: Dict[str, Any]
    collected_eggs: Dict[str, Any]

class Easter(BaseModel):
    rabbits: EasterRabbits
    time_tower: Dict[str, Any]
    shop: Dict[str, Any]
    employees: Dict[str, Any]
    chocolate: int
    total_chocolate: int
    chocolate_since_prestige: int

class Events(BaseModel):
    easter: Easter

class AccessoryBagStorage(BaseModel):
    tuning: Dict[str, Any]

class Leveling(BaseModel):
    completions: Dict[str, Any]
    experience: int

class JacobsContest(BaseModel):
    medals_inv: Dict[str, Any]
    perks: Dict[str, Any]
    contests: Dict[str, Any]

class Catacombs(BaseModel):
    watcher_kills: Dict[str, Any]
    fastest_time_s: Dict[str, Any]
    fastest_time: Dict[str, Any]
    most_damage_healer: Dict[str, Any]
    fastest_time_s_plus: Dict[str, Any]
    most_healing: Dict[str, Any]
    most_damage_tank: Dict[str, Any]
    best_score: Dict[str, Any]
    most_damage_archer: Dict[str, Any]
    mobs_killed: Dict[str, Any]
    most_mobs_killed: Dict[str, Any]
    most_damage_berserk: Dict[str, Any]
    tier_completions: Dict[str, Any]
    most_damage_mage: Dict[str, Any]

class DungeonTypes(BaseModel):
    catacombs: Catacombs
    master_catacombs: Dict[str, Any]

class PlayerClasses(BaseModel):
    healer: Dict[str, Any]
    mage: Dict[str, Any]
    berserk: Dict[str, Any]
    archer: Dict[str, Any]
    tank: Dict[str, Any]

class Dungeons(BaseModel):
    dungeon_types: DungeonTypes
    player_classes: PlayerClasses
    dungeon_journal: Dict[str, Any]

class MemberProfile(BaseModel):
    first_join: int
    cookie_buff_active: bool

class NetherQuests(BaseModel):
    quest_data: Dict[str, Any]
    miniboss_daily: Dict[str, Any]
    kuuda_boss_daily: Dict[str, Any]
    quest_rewards: Dict[str, Any]
    alchemist_quest: Dict[str, Any]
    rulenor: Dict[str, Any]
    chicken_quest: Dict[str, Any]
    pomtair_quest: Dict[str, Any]
    suus_quest: Dict[str, Any]
    pablo_quest: Dict[str, Any]
    duel_training_quest: Dict[str, Any]
    sirih_quest: Dict[str, Any]
    edelis_quest: Dict[str, Any]
    mollim_quest: Dict[str, Any]
    aranya_quest: Dict[str, Any]

class Abiphone(BaseModel):
    contact_data: Dict[str, Any]
    games: Dict[str, Any]

class NetherIslandPlayerData(BaseModel):
    quests: NetherQuests
    kuudra_completed_tiers: Dict[str, Any]
    dojo: Dict[str, Any]
    abiphone: Abiphone
    matriarch: Dict[str, Any]

class MiningCore(BaseModel):
    hotm_migrator_tree_reset_send_message: bool

class PetsData(BaseModel):
    pets: List[Any]

class Bestiary(BaseModel):
    migrated_stats: bool

class Forge(BaseModel):
    forge_processes: Dict[str, Any]

class FairySoul(BaseModel):
    total_collected: int

class TrophyFish(BaseModel):
    rewards: List[Any]

class ObjectiveDetail(BaseModel):
    status: str
    progress: int
    completed_at: int

class Objectives(BaseModel):
    collect_log: ObjectiveDetail
    talk_to_guide: ObjectiveDetail
    public_island: ObjectiveDetail
    craft_workbench: ObjectiveDetail
    craft_wood_pickaxe: ObjectiveDetail
    explore_hub: ObjectiveDetail
    explore_village: ObjectiveDetail
    talk_to_librarian: ObjectiveDetail
    talk_to_farmer: ObjectiveDetail
    talk_to_blacksmith: ObjectiveDetail
    talk_to_lumberjack: ObjectiveDetail
    talk_to_event_master: ObjectiveDetail
    talk_to_auction_master: ObjectiveDetail
    talk_to_banker: ObjectiveDetail
    talk_to_fairy: ObjectiveDetail
    talk_to_fisherman_1: ObjectiveDetail
    talk_to_carpenter: ObjectiveDetail
    paint_canvas: ObjectiveDetail
    talk_to_pet_collector: ObjectiveDetail
    talk_to_pet_sitter: ObjectiveDetail
    tutorial: List[str]

class SlayerDetail(BaseModel):
    claimed_levels: Dict[str, Any]

class SlayerBosses(BaseModel):
    zombie: SlayerDetail
    enderman: SlayerDetail
    spider: SlayerDetail
    wolf: SlayerDetail
    blaze: Dict[str, Any]

class Slayer(BaseModel):
    slayer_bosses: SlayerBosses

class Member(BaseModel):
    player_data: PlayerData
    events: Events
    accessory_bag_storage: AccessoryBagStorage
    leveling: Leveling
    jacobs_contest: JacobsContest
    dungeons: Dungeons
    profile: MemberProfile
    player_id: str
    nether_island_player_data: NetherIslandPlayerData
    mining_core: MiningCore
    pets_data: PetsData
    bestiary: Bestiary
    quests: Dict[str, Any]
    forge: Forge
    fairy_soul: FairySoul
    trophy_fish: TrophyFish
    objectives: Objectives
    slayer: Slayer

class PlayerProfile(BaseModel):
    profile_id: str
    members: Dict[str, Member]

class Profile(BaseModel):
    success: bool
    profile: PlayerProfile