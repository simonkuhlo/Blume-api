from pydantic import BaseModel
from schemas.answer_type import AnswerType

class Read(BaseModel):
    id: int
    title: str
    description: str
    #answer_type: AnswerType

    class Config:
        from_attributes = True