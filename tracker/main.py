from fastapi import APIRouter

from tracker.routers import tasks


api_router = APIRouter()

api_router.include_router(tasks.router, prefix="/tasks", tags=["users"])
