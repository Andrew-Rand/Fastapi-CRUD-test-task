from pydantic import BaseModel
from datetime import datetime

class ArticleCreate(BaseModel):
    title: str
    content: str
    author_id: int | None = None

class ArticleUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    author_id: int | None = None

class ArticleOut(BaseModel):
    id: int
    title: str
    content: str
    author_id: int | None = None
    created_at: datetime

    class Config:
        orm_mode = True
