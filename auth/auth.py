import fastapi as fa
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import orm

from core import db
from users.repositories.users_repository import UsersRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db_session: orm.Session = fa.Depends(db.get_session)
):
    # jwt auth using token
    user_id = "7725640d-477a-45d6-b0ce-3d1c905426f1"

    return await UsersRepository(db_session=db_session).get_user_by_id(user_id)
