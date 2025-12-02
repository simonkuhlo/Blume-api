from pydantic import BaseModel

class Read(BaseModel):
    id: int
    name: str
    admin: bool

    class Config:
        from_attributes = True