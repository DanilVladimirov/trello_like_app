import uuid

import pydantic as p

from tracker.models import TaskStatus
from users.schemas import UserInfoSchema


class TaskUpdateSchema(p.BaseModel):
    name: str
    description: str
    owner_id: uuid.UUID | None
    user_ids: list[uuid.UUID] = []
    status: TaskStatus

    class Config:
        orm_mode = True


class TaskUpdatedResponse(p.BaseModel):
    name: str
    description: str
    owner_id: uuid.UUID | None
    users: list[UserInfoSchema] = []
    status: TaskStatus

    class Config:
        orm_mode = True
