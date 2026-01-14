from fastapi import APIRouter
from app.schemas.task import TaskCreate, TaskResponse

router = APIRouter(
    prefix="/api/v1/tasks",
    tags=["Tasks"]
)

@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate):
    return {
        "id": 1,
        "title": task.title,
        "description": task.description,
        "completed": False
    }
