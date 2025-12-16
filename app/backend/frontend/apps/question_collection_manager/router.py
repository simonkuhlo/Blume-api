from typing import Annotated, Optional
from fastapi import APIRouter, Form
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from frontend.jinja_templates import templates
from crud import question_collection as question_collection_crud
from crud import question as question_crud
from schemas.question_collection import QuestionCollectionUpdate, QuestionCollectionRead, QuestionCollectionCreate
from frontend.utils.item_browser import ItemBrowser, ItemBrowserObject, ItemBrowserObjectButton
from data.utils.question_question_collection_relation import modify_questions_of_collection
from . import helpers

router = APIRouter(prefix="/question_collection_manager", tags=["question_collection_manager"])

@router.get("/", response_class=HTMLResponse)
async def main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("apps/admin/question_collection_manager/question_collection_manager.j2", {"request": request})

@router.get("/browser", response_class=HTMLResponse)
async def render_question_collection_browser(request: Request) -> HTMLResponse:
    browser = helpers.get_question_collection_browser()
    return browser.render(request)

@router.get("/browser/create_collection", response_class=HTMLResponse)
async def create_collection_from_browser(request: Request) -> HTMLResponse:
    question_collection_crud.create(QuestionCollectionCreate())
    return helpers.get_question_collection_browser().render(request)

@router.get("/editor/{collection_id}/question_relation_browser", response_class=HTMLResponse)
async def relation_browser(request: Request, collection_id: int) -> HTMLResponse:
    question_collection = question_collection_crud.get(collection_id)
    return helpers.create_question_relation_browser(question_collection).render(request)

@router.get("/editor", response_class=HTMLResponse)
@router.get("/editor/{collection_id}", response_class=HTMLResponse)
async def collection_editor(request: Request, collection_id: Optional[int] = None, reload_browser: bool = False) -> HTMLResponse:
    question_collection = None
    related_question_ids = []
    all_questions = []
    if collection_id:
        question_collection = question_collection_crud.get(collection_id)
        related_question_ids = []
        for question in question_collection.questions:
            related_question_ids.append(question.id)
        all_questions = question_crud.list()
    return templates.TemplateResponse("apps/admin/question_collection_manager/question_collection_editor.j2",
                                      {"request": request,
                                       "question_collection": question_collection,
                                       "related_question_ids": related_question_ids,
                                       "all_questions": all_questions,
                                       "reload_browser": reload_browser
                                       })

@router.put("/editor/{collection_id}", response_class=HTMLResponse)
async def update_from_form(request: Request, collection_id: int, title: Annotated[str, Form()], description: Annotated[str, Form()]) -> HTMLResponse:
    collection = question_collection_crud.get(collection_id)
    updated_collection = QuestionCollectionUpdate.model_validate(collection)
    updated_collection.title = title
    updated_collection.description = description
    question_collection_crud.update(collection_id, updated_collection)
    return await collection_editor(request, collection_id, True)

@router.delete("/editor/{collection_id}", response_class=HTMLResponse)
async def update_from_form(request: Request, collection_id: int) -> HTMLResponse:
    question_collection_crud.delete(collection_id)
    return await collection_editor(request, None, True)

@router.get("/editor/{collection_id}/add_question/{question_id}")
async def add_question(
        request: Request,
        collection_id: int,
        question_id: int,
):
    modify_questions_of_collection(collection_id, question_id)
    return ItemBrowserObjectButton(
                on_click_url=f"/admin/question_collection_manager/editor/{collection_id}/remove_question/{question_id}",
                name="Remove",
    ).render(request)

@router.get("/editor/{collection_id}/remove_question/{question_id}")
async def remove_question(
        request: Request,
        collection_id: int,
        question_id: int,
):
    modify_questions_of_collection(collection_id, question_id, True)
    return ItemBrowserObjectButton(
        on_click_url=f"/admin/question_collection_manager/editor/{collection_id}/add_question/{question_id}",
        name="Add",
    ).render(request)