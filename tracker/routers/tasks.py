import fastapi as fa
from sqlalchemy.ext.asyncio import AsyncSession

from auth.roles import RoleChecker
from core.db import get_session
from tracker.background_tasks import send_task_change_email
from tracker.repositories.tasks_repository import TasksRepository
from tracker.schemas import TaskUpdateSchema, TaskUpdatedResponse

router = fa.APIRouter()


@router.put(
    "/{task_id}",
    response_model=TaskUpdatedResponse,
    dependencies=[fa.Depends(RoleChecker(allowed_roles=['admin']))]
)
async def edit_task(
    task_id: str,
    task_update_data: TaskUpdateSchema,
    background_tasks: fa.BackgroundTasks,
    db: AsyncSession = fa.Depends(get_session),
):
    task_repo = TasksRepository(db_session=db)
    task = await task_repo.get_task_by_id_with_users(task_id)

    if not task:
        raise

    await task_repo.update_task(task, task_update_data)

    await db.refresh(task)

    if task.owner:
        background_tasks.add_task(send_task_change_email, task)

    return task
