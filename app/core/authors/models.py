import typing

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.common.db.base_columns import UUIDKeyType
from app.common.db.base_models import Model


class Author(Model):
    __tablename__ = "authors"

    uuid: Mapped[UUIDKeyType]
    name: Mapped[str] = mapped_column(sa.String(255))