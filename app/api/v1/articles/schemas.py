from pydantic import BaseModel
from datetime import datetime

class ArticleOut(BaseModel):
    id: int
    title: str
    content: str
    author_id: int | None = None
    created_at: datetime

    class Config:
        orm_mode = True