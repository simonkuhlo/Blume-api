from fastapi import FastAPI
from routes.crud.entries import router as entries_router
from routes.crud.users import router as users_router
from routes.crud.questions import router as questions_router
from routes.crud.question_collections import router as question_collections_router
from routes.crud.answers import router as answers_router

title: str = "Blume"
summary: str = ""
description: str = ""
version: str = "0.0.1"

app = FastAPI(title=title, summary=summary, description=description, version=version)
app.include_router(entries_router)
app.include_router(users_router)
app.include_router(questions_router)
app.include_router(question_collections_router)
app.include_router(answers_router)
