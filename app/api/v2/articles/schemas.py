from pydantic import BaseModel
from datetime import datetime

class ArticleOutSimple(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        orm_mode = True
