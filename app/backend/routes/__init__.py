from fastapi import APIRouter
from .crud import users, answers, entries, question_collections, questions
from . import entry_service

main_router = APIRouter()
main_router.include_router(users.router, tags=["users"])
main_router.include_router(answers.router, tags=["answers"])
main_router.include_router(entries.router, tags=["entries"])
main_router.include_router(question_collections.router, tags=["question_collections"])
main_router.include_router(questions.router, tags=["questions"])
main_router.include_router(entry_service.router)
