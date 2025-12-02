from pydantic import BaseModel
from ..answer_type import AnswerType

class Update(BaseModel):
    title: str
    description: str
    #answer_type: AnswerType