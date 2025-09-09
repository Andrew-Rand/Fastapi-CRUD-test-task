import typing
import uuid

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from app.common.db.base_columns import IntPk, AutoCreatedAt, AutoUpdatedAt


class Base(DeclarativeBase):
    __abstract__ = True


class Model(Base):
    """Base model class. SQLA entities should extend this class."""

    __abstract__ = True

    id: Mapped[IntPk]
    created_at: Mapped[AutoCreatedAt | None]
    updated_at: Mapped[AutoUpdatedAt | None]