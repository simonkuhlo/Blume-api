from .crud_handler_router import CRUDHandlerRouter
from crud import question_collection

router = CRUDHandlerRouter(question_collection)