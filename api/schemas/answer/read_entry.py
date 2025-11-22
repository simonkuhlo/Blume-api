from pydantic import BaseModel
from ..user import UserRead
from ..question import QuestionRead
from ..entry import EntryRead

class EntryAnswerRead(BaseModel):
    id: int
    question: QuestionRead
    entry: EntryRead
    string_value: str
