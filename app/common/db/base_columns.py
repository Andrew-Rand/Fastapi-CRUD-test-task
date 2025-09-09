import typing
import uuid

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# TODO: maybe move columns to separate file
IntPk = typing.Annotated[int, mapped_column(sa.Integer, primary_key=True, autoincrement=True)]
UUIDKeyType = typing.Annotated[
    str, mapped_column(sa.String(36), default=lambda: uuid.uuid4().hex, index=True, unique=True)
]
AutoCreatedAt = typing.Annotated[
    datetime.datetime,
    mapped_column(
        sa.DateTime,
        default_factory=lambda: datetime.datetime.now(datetime.UTC),
        server_default=sa.func.now(),
    ),
]
AutoUpdatedAt = typing.Annotated[
    datetime.datetime,
    mapped_column(
        sa.DateTime,
        server_default=sa.func.now(),
        server_onupdate=sa.func.now(),
        onupdate=sa.func.now(),
        default_factory=lambda: datetime.datetime.now(datetime.UTC),
    ),
]
