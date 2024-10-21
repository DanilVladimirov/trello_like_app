from fastapi import FastAPI
import asyncio
from tracker.main import api_router as tasks_api_router


app = FastAPI()

app.include_router(tasks_api_router)


async def init_test_data():
    from sqlalchemy.ext.asyncio.session import AsyncSession
    from core.db import engine
    from tracker.models import Task
    from users.models import User, Role
    from sqlalchemy.future import select

    async with AsyncSession(engine) as db_session:

        roles = await db_session.scalars(select(Role))

        roles = roles.all()

        if not roles:
            db_session.add(Role(name="admin"))
            db_session.add(Role(name="worker"))


        user_id = "7725640d-477a-45d6-b0ce-3d1c905426f1"
        user_id2 = "7725640d-477a-45d6-b0ce-3d1c905426f2"
        task_id = "df176e79-a72f-44f4-b0bc-b4c2b205c83b"

        user1 = await db_session.scalar(select(User).where(User.id == user_id))
        user2 = await db_session.scalar(select(User).where(User.id == user_id2))

        if not user1:
            user1 = User(email="test@test.com", password="wegwegegew", id=user_id, role_id="admin")
            db_session.add(user1)

        if not user2:
            user2 = User(email="test2@test.com", password="wegwegegew", id=user_id2, role_id="worker")
            db_session.add(user2)

        task = await db_session.scalar(select(Task).where(Task.id == task_id))

        if not task:
            task = Task(id=task_id, owner_id=user_id, description="vzvsdvv", name="test task")

            task.users.append(user1)
            task.users.append(user2)

            db_session.add(task)

        await db_session.commit()


loop = asyncio.get_running_loop()

asyncio.ensure_future(init_test_data(), loop=loop)

