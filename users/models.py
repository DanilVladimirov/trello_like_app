import sqlalchemy as sa
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import relationship, backref

from core import db
from core.db import Base


class Role(db.Base):
    __tablename__ = "role"

    name: str = Column(sa.String(length=255), primary_key=True)


association_table = Table(
    "user_task_association",
    Base.metadata,
    Column("task_id", ForeignKey("task.id"), primary_key=True),
    Column("user_id", ForeignKey("user.id"), primary_key=True),
)


class User(db.Base):
    __tablename__ = "user"

    id = Column(sa.UUID, primary_key=True)
    email = Column(sa.String, unique=True)
    password = Column(sa.String(length=42))

    role_id = Column(sa.String, sa.ForeignKey("role.name"), nullable=True)
    role = relationship(Role, backref=backref("users"), foreign_keys=role_id)

    tasks = relationship("Task", secondary=association_table)
