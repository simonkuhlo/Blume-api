from pydantic import BaseModel
from ..answer.read_entry import AnswerReadEntry
from ..user import UserRead


class EntryRead(BaseModel):
    id: int
    user: UserRead
    answers: list[AnswerReadEntry]