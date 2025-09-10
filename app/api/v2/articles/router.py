from fastapi import APIRouter, HTTPException

from app.api.v2.articles.schemas import ArticleOutSimple
from app.core.articles.queries import get_article, get_articles
from app.core.dependencies import DbSession, Pagination

router = APIRouter(prefix="/v2")

@router.get("/articles/{article_id}", response_model=ArticleOutSimple)
async def read(article_id: int, dbsession: DbSession):
    article = await get_article(dbsession, article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@router.get("/articles", response_model=list[ArticleOutSimple])
async def read_all(pagination: Pagination, dbsession: DbSession):
    return await get_articles(dbsession, pagination.offset, pagination.limit)
