from fastapi import APIRouter, HTTPException

from app.core.articles.queries import create_article, get_article, get_articles, update_article, delete_article
from app.core.articles.schemas import ArticleOut, ArticleCreate, ArticleUpdate
from app.core.dependencies import DbSession

router = APIRouter()

@router.post("/articles", response_model=ArticleOut)
async def create(data: ArticleCreate, dbsession: DbSession):
    new_article = await create_article(dbsession, data)
    return new_article

@router.get("/articles/{article_id}", response_model=ArticleOut)
async def read(article_id: int, dbsession: DbSession):
    article = await get_article(dbsession, article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@router.get("/articles", response_model=list[ArticleOut])
async def read_all(dbsession: DbSession):
    # TODO: add pagination
    return await get_articles(dbsession)

@router.patch("/articles/{article_id}", response_model=ArticleOut)
async def update(article_id: int, data: ArticleUpdate, dbsession: DbSession):
    article = await update_article(dbsession, article_id, data)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@router.delete("/articles/{article_id}")
async def delete(article_id: int, dbsession: DbSession):
    success = await delete_article(dbsession, article_id)
    if not success:
        raise HTTPException(status_code=404, detail="Article not found")
    return {"detail": "Deleted"}