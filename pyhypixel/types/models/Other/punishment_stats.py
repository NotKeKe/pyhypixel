from pydantic import BaseModel

class PunishmentStats(BaseModel):
    '''Punishment Statistics\n`v2/punishmentstats`'''
    success: bool
    watchdog_lastMinute: int
    staff_rollingDaily: int
    watchdog_total: int
    watchdog_rollingDaily: int
    staff_total: int