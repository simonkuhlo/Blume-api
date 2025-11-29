#add / remove a default collection of questions for an entry
from sqlalchemy.orm import Session
from models import Question, QuestionCollection


def add_default_questions(session: Session):
    question_collection = QuestionCollection(
        title='Default',
        questions=[
            Question(
                title="Name",
                description="What is your name?",
                     ),
            Question(
                title="Age",
                description="How old are you?",
            ),
            Question(
                title="Dream",
                description="What do you want to do when you are older?",
            )
        ]
    )
    session.add(question_collection)
    session.commit()