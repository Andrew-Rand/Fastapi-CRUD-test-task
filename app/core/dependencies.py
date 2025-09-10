import typing

from fastapi import Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.common.db.engine import new_session


async def get_dbsession() -> typing.AsyncGenerator[AsyncSession, None]:
    """Create a new database session for the request."""
    async with new_session() as dbsession:
        yield dbsession


class PaginationModel(BaseModel):
    offset: int = 0
    limit: int = 10

def get_pagination(offset: int = 0, limit: int = 10) -> PaginationModel:
    return PaginationModel(offset=offset, limit=limit)


DbSession = typing.Annotated[AsyncSession, Depends(get_dbsession)]
Pagination = typing.Annotated[dict, Depends(get_pagination)]
