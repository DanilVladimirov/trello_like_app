import uuid

import pydantic as p


class UserInfoSchema(p.BaseModel):
    id: uuid.UUID
    email: str
    role_id: str
