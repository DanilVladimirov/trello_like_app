from typing import Annotated

import fastapi as fa

from auth.auth import get_current_user
from users.models import User


class RoleChecker:
    def __init__(self, allowed_roles):
        self.allowed_roles = allowed_roles

    def __call__(self, user: Annotated[User, fa.Depends(get_current_user)]):
        if user.role_id in self.allowed_roles:
            return True

        raise fa.HTTPException(
            status_code=fa.status.HTTP_401_UNAUTHORIZED,
            detail="You don't have enough permissions")
