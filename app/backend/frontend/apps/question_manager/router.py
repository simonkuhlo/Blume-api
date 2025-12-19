from typing import Annotated, Optional
from fastapi import APIRouter, Form
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from frontend.jinja_templates import templates
from crud import question_collection as question_collection_crud
from crud import question as question_crud
from schemas.question import QuestionUpdate, QuestionCreate
from schemas.question_collection import QuestionCollectionUpdate, QuestionCollectionRead, QuestionCollectionCreate
from frontend.utils.item_browser import ItemBrowser, ItemBrowserObject, ItemBrowserObjectButton
from data.utils.question_question_collection_relation import modify_questions_of_collection
from . import helpers

router = APIRouter(prefix="/question_manager", tags=["question_collection_manager"])

@router.get("/", response_class=HTMLResponse)
async def admin_question_manager(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("apps/admin/question_manager/question_manager_app.j2", {"request": request})

@router.get("/browser", response_class=HTMLResponse)
async def question_browser(request: Request) -> HTMLResponse:
    browser = helpers.create_question_browser()
    return browser.render(request=request)

@router.get("/browser/create_question", response_class=HTMLResponse)
async def create_question(request: Request) -> HTMLResponse:
    question_crud.create(QuestionCreate())
    return await question_browser(request)

@router.get("/editor/{question_id}", response_class=HTMLResponse)
async def question_editor(request: Request, question_id: int, reload_browser: bool = False) -> HTMLResponse:
    question = question_crud.get(question_id)
    return templates.TemplateResponse("apps/admin/question_manager/question_editor.j2", {"request": request,
                                                                                         "question": question,
                                                                                         "reload_browser": reload_browser
                                                                                         })

@router.put("/editor/{question_id}", response_class=HTMLResponse)
async def update_from_form(request: Request, question_id: int, title: Annotated[str, Form()], description: Annotated[str, Form()], short: Annotated[bool, Form()] = False) -> HTMLResponse:
    question = question_crud.get(question_id)
    updated_question = QuestionUpdate.model_validate(question)
    updated_question.title = title
    updated_question.description = description
    updated_question.short = short
    question_crud.update(question_id, updated_question)
    return await question_editor(request, question_id, True)