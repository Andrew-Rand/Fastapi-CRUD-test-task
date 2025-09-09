import typing

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.common.db.engine import new_session


async def get_dbsession() -> typing.AsyncGenerator[AsyncSession, None]:
    """Create a new database session for the request."""
    async with new_session() as dbsession:
        yield dbsession


DbSession = typing.Annotated[AsyncSession, Depends(get_dbsession)]