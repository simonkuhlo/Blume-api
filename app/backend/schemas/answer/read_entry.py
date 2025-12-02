from typing import Optional
from pydantic import BaseModel
from ..question import QuestionRead

class EntryAnswerRead(BaseModel):
    id: int
    question: Optional[QuestionRead] = None
    value: str

    class Config:
        from_attributes = True