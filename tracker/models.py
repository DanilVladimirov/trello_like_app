import uuid
from enum import Enum

from sqlalchemy.dialects import postgresql
from sqlalchemy import orm
from core.db import Base
from sqlalchemy.orm import Mapped
from users.models import User, association_table
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class TaskStatus(str, Enum):
    TODO = "TODO"
    IN_PROGRESS = "In progress"
    DONE = "Done"


class Task(Base):
    __tablename__ = "task"

    id: uuid.UUID = sa.Column(sa.UUID, primary_key=True)
    name: str = sa.Column(sa.String(length=255))
    description: str = sa.Column(sa.String(length=1000))
    owner_id = sa.Column(postgresql.UUID(as_uuid=True), sa.ForeignKey("user.id"), nullable=True)
    owner = relationship(
        "users.models.User",
        backref=orm.backref("owned_tasks"),
        foreign_keys=owner_id,
    )
    users: Mapped[list[User]] = relationship(back_populates="tasks", secondary=association_table)

    status: TaskStatus = sa.Column(sa.String, default=TaskStatus.TODO.value)
