from typing import Optional
from schemas.entry import EntryRead
from schemas.answer import AnswerRead, EntryAnswerRead
from schemas.question import QuestionRead
from schemas.user import UserRead

def get_entry_data(entry_id:int) -> Optional[EntryRead]:
    if entry_id < 0:
        return None
    fake_question = QuestionRead(
        id = 0,
        title = "Fake Question",
        description = "Fake Question",
    )
    fake_answer = EntryAnswerRead(
        id = entry_id,
        question = fake_question,
        string_value = "Fake Answer",
    )
    fake_user = UserRead(
        id = entry_id,
        name = "Fake User",
        admin = False
    )
    fake_entry = EntryRead(
        id = entry_id,
        user = fake_user,
        answers = [fake_answer, fake_answer, fake_answer, fake_answer, fake_answer],
    )
    return fake_entry