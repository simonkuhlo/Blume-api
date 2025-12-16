from typing import Optional
from pydantic import BaseModel
from .answer_type import AnswerType

class QuestionRef(BaseModel):
    id: int

    class Config:
        from_attributes = True

class QuestionCreate(BaseModel):
    title: str = "Unnamed Question"
    description: Optional[str] = ""
    short: Optional[bool] = False
    #answer_type: AnswerType

class QuestionRead(BaseModel):
    id: int
    title: str
    description: str
    short: bool = False
    #answer_type: AnswerType

    class Config:
        from_attributes = True

class QuestionUpdate(BaseModel):
    title: str
    description: str
    short: Optional[bool] = False
    #answer_type: AnswerType

    class Config:
        from_attributes = True