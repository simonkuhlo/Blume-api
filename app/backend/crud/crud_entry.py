from data.database import session
from models import Entry
from schemas.entry import EntryRead, EntryCreate, EntryUpdate
from .base import CRUDHandler

class EntryCRUD(CRUDHandler[Entry, EntryRead, EntryCreate, EntryUpdate]):

    def __init__(self):
        super().__init__("entry", session, Entry, EntryRead, EntryCreate, EntryUpdate)

handler: EntryCRUD = EntryCRUD()