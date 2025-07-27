from pydantic import BaseModel, Field
from typing import Optional

class ErrorResponse(BaseModel):
    '''Error if hypixel return 200 but not success'''
    success: bool
    cause: str
    throttle: Optional[bool] = None
    global_: Optional[bool] = Field(None, alias="global")

    model_config = {
        "populate_by_name": True
    }