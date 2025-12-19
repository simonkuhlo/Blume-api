from crud import question as question_crud
from schemas.question_collection import QuestionCollectionUpdate, QuestionCollectionRead, QuestionCollectionCreate
from frontend.utils.item_browser import ItemBrowser, ItemBrowserObject, ItemBrowserObjectButton

def create_question_browser() -> ItemBrowser:
    questions = question_crud.list()
    browser_objects = []
    for question in questions:
        browser_objects.append(
            ItemBrowserObject(
                title=f"{question.id} - {question.title}",
                on_click_url=f"/admin/question_manager/editor/{question.id}",
                buttons=[],
            )
        )
    browser = ItemBrowser(
        name="Question relation browser",
        refresh_url=f"/admin/question_manager/browser",
        objects=browser_objects,
        toolbar_buttons=[
            ItemBrowserObjectButton(
                on_click_url="/admin/question_manager/browser/create_question",
                name="+ New Question",
                hx_target="closest .browser_frame",
                hx_swap="outerHTML"
            )
        ],
    )
    return browser