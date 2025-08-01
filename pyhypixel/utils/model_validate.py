from typing import Union

from ..types.models.error import ErrorResponse

def model_validate(_class: object, data: Union[list, dict]) -> object:
    return _class.model_validate(data) if data.get('success') else ErrorResponse.model_validate(data)