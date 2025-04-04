import uuid

import inflect
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, declarative_mixin, declared_attr

Base = declarative_base()

inflector = inflect.engine()


@declarative_mixin
class BaseMixin:
    """
    Class defining common attributes for all models.
    All models should inherit from this class.
    """

    uuid = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )

    @declared_attr
    def __tablename__(cls) -> str:
        """
        Returns the pluralized class name as the table name.
        """
        return inflector.plural(cls.__name__.lower())
