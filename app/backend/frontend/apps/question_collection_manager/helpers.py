from crud import question_collection as question_collection_crud
from crud import question as question_crud
from schemas.question_collection import QuestionCollectionUpdate, QuestionCollectionRead, QuestionCollectionCreate
from frontend.utils.item_browser import ItemBrowser, ItemBrowserObject, ItemBrowserObjectButton

def get_question_collection_browser() -> ItemBrowser:
    browser: ItemBrowser = ItemBrowser(
        name="Question collection browser",
        refresh_url="/admin/question_collection_manager/browser",
        toolbar_buttons=[
            ItemBrowserObjectButton(
                on_click_url="/admin/question_collection_manager/browser/create_collection",
                name="+ New Collection",
                hx_target="closest .browser_frame",
                hx_swap="outerHTML"
            )
        ]
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


def create_question_relation_browser(question_collection: QuestionCollectionRead) -> ItemBrowser:
    questions = question_crud.list()
    related_question_ids = []
    for question in question_collection.questions:
        related_question_ids.append(question.id)
    browser_objects = []
    for question in questions:
        if question.id in related_question_ids:
            button = ItemBrowserObjectButton(
                on_click_url=f"/admin/question_collection_manager/editor/{ question_collection.id }/remove_question/{ question.id }",
                name="Remove",
            )
        else:
            button = ItemBrowserObjectButton(
                on_click_url=f"/admin/question_collection_manager/editor/{question_collection.id}/add_question/{question.id}",
                name="Add",
            )
        browser_objects.append(
            ItemBrowserObject(
                title=f"{question.id} - {question.title}",
                on_click_url=None,
                buttons=[button],
            )
        )
    browser = ItemBrowser(
        name="Question relation browser",
        refresh_url=f"/admin/question_collection_manager/editor/{question_collection.id}/question_relation_browser",
        objects=browser_objects,
    )
    return browser