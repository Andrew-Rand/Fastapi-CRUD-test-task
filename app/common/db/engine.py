import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:postgres@localhost:5432/articles_db")

engine = create_async_engine(
    'postgresql+asyncpg://postgres:postgres@db/articles_db',
    echo=True,
    future=True,
)
new_session = async_sessionmaker(engine, expire_on_commit=False)
