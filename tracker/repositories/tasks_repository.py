from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

from tracker.models import Task
from users.models import User
from tracker.schemas import TaskUpdateSchema


class TasksRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    async def get_task_by_id_with_users(self, task_id):
        return await self.db_session.scalar(select(Task).where(Task.id == task_id).options(
            joinedload(Task.users), joinedload(Task.owner))
        )

    async def update_task(self, task, task_update_data: TaskUpdateSchema):
        task_update_data = task_update_data.dict()
        user_ids = task_update_data.pop('user_ids')

        for var, value in task_update_data.items():
            setattr(task, var, value) if value else None

        users = await self.db_session.scalars(select(User).where(User.id.in_(user_ids)))

        users = users.all()

        task.users = users

        await self.db_session.commit()
