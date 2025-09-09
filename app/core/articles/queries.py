import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.core.articles.models import Article
from app.core.articles.schemas import ArticleCreate, ArticleUpdate


async def get_article(db: AsyncSession, article_id: int) -> Article | None:
    """Get exactly one row from the database, else return None"""
    stmt = (
        sa.select(Article)
        .where(Article.id == article_id)
        # .options(sa.orm.joinedload(Article.author)
    )
    result = await db.scalars(stmt)
    return result.one_or_none()

async def get_articles(db: AsyncSession) -> list[type[Article]]:
    """Get all rows from the database matching the query."""
    stmt = (
        sa.select(Article)
    )
    result = await db.scalars(stmt)
    return result.all()

async def create_article(db: AsyncSession, data: ArticleCreate) -> Article:
    article = Article(**data.model_dump(exclude_none=True))
    db.add(article)
    await db.commit()
    await db.refresh(article)
    return article

async def update_article(db: AsyncSession, article_id: int, data: ArticleUpdate) -> Article | None:
    article = await get_article(db, article_id)
    if not article:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(article, field, value)
    await db.commit()
    await db.refresh(article)
    return article

async def delete_article(db: AsyncSession, article_id: int) -> bool:
    article = await get_article(db, article_id)
    if not article:
        return False
    await db.delete(article)
    await db.commit()
    return True
