from pydantic import BaseModel
from ..answer.read_entry import EntryAnswerRead
from ..user import UserRead


class EntryRead(BaseModel):
    id: int
    user: UserRead
    answers: list[EntryAnswerRead]

    class Config:
        from_attributes = True