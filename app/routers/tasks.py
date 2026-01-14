from fastapi import APIRouter
from app.schemas.task import TaskCreate

router = APIRouter(
    prefix="/api/v1/tasks",
    tags=["Tasks"]
)

@router.post("/")
def create_task(task: TaskCreate):
    return {
        "message": "Task created successfully",
        "task": task
    }
