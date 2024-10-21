from sqlalchemy.future import select

from users.models import User


class UsersRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    async def get_user_by_id(self, user_id):
        return await self.db_session.scalar(
            select(User)
            .where(User.id == user_id)
        )
