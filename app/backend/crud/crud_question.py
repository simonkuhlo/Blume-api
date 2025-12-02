from data.database import session
from models import Question
from schemas.question import QuestionRead, QuestionCreate, QuestionUpdate
from .base import CRUDHandler

class QuestionCRUD(CRUDHandler[Question, QuestionRead, QuestionCreate, QuestionUpdate]):

    def __init__(self):
        super().__init__("question", session, Question, QuestionRead, QuestionCreate, QuestionUpdate)

handler: QuestionCRUD = QuestionCRUD()