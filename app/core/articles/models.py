import typing

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.common.db.base_columns import UUIDKeyType
from app.common.db.base_models import Model
from app.core.authors.models import Author


class Article(Model):
    __tablename__ = "articles"

    uuid: Mapped[UUIDKeyType]
    title: Mapped[str] = mapped_column(sa.String(255))
    content: Mapped[str] = mapped_column(sa.Text)

    author_id: Mapped[int] = mapped_column(sa.ForeignKey("authors.id"), nullable=True)