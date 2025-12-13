from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from frontend.jinja_templates import templates
from crud import question_collection as question_collection_crud
from crud import question as question_crud
from schemas.question_collection import QuestionCollectionUpdate
from frontend.utils.item_browser import ItemBrowser, ItemBrowserObject, ItemBrowserObjectButton

router = APIRouter(prefix="/question_collection_manager", tags=["question_collection_manager"])

@router.get("/", response_class=HTMLResponse)
async def main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("apps/admin/question_collection_manager/question_collection_manager.j2", {"request": request})

def get_question_collection_browser() -> ItemBrowser:
    browser: ItemBrowser = ItemBrowser(
        name="Question Collections",
        refresh_url=None,
    )

    question_collections = question_collection_crud.list()
    browser.objects = []
    for question_collection in question_collections:
        browser.objects.append(
            ItemBrowserObject(
                title=f"{question_collection.id} - {question_collection.title}",
                on_click_url=f"/admin/question_collection_manager/editor/{question_collection.id}",
            )
        )
    return browser

@router.get("/browser", response_class=HTMLResponse)
async def render_question_collection_browser(request: Request) -> HTMLResponse:
    browser = get_question_collection_browser()
    return templates.TemplateResponse("apps/admin/question_collection_manager/question_collection_browser.j2",
                                      {"request": request, "browser": browser})

@router.get("/editor/{collection_id}", response_class=HTMLResponse)
async def admin_question_editor(request: Request, collection_id: int) -> HTMLResponse:
    question_collection = question_collection_crud.get(collection_id)
    related_questions = None
    unrelated_questions = question_crud.list()
    return templates.TemplateResponse("apps/admin/question_collection_manager/question_collection_editor.j2",
                                      {"request": request,
                                       "question_collection": question_collection,
                                       "related_questions": related_questions,
                                       "unrelated_questions": unrelated_questions
                                       })

@router.put("/editor/{collection_id}/add_question/{question_id}")
async def add_question(
        request: Request,
        collection_id: int,
        question_id: int,
):
    collection = question_collection_crud.get(collection_id)
    collection.questions.append(question_collection_crud.get(question_id))
    question_collection = question_collection_crud.update(collection.id, QuestionCollectionUpdate.model_validate(collection))
    return question_collection

@router.put("/editor/{collection_id}/remove_question/{question_id}")
async def remove_question(
        request: Request,
        collection_id: int,
        question_id: int,
):
    pass