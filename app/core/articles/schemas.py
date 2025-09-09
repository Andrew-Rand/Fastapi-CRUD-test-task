from pydantic import BaseModel


class ArticleCreate(BaseModel):
    title: str
    content: str
    author_id: int | None = None

class ArticleUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    author_id: int | None = None