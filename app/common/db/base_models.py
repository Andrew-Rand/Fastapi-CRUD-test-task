from sqlalchemy.orm import DeclarativeBase, Mapped

from app.common.db.base_columns import AutoCreatedAt, AutoUpdatedAt, IntPk


class Base(DeclarativeBase):
    __abstract__ = True


class Model(Base):
    """Base model class. SQLA entities should extend this class."""

    __abstract__ = True

    id: Mapped[IntPk]
    created_at: Mapped[AutoCreatedAt | None]
    updated_at: Mapped[AutoUpdatedAt | None]