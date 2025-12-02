from enum import Enum
from typing import Union
from pydantic import BaseModel

class BaseAnswerType(BaseModel):
    name:str = "string"

AnswerType = Union[BaseAnswerType]