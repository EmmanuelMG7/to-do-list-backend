from fastapi import APIRouter
from app.schemas.task import TaskCreate, TaskResponse
from typing import List


tasks_db = []

router = APIRouter(
    prefix="/api/v1/tasks",
    tags=["Tasks"]
)

@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate):
    new_task = {
        "id": len(tasks_db) + 1,
        "title": task.title,
        "description": task.description,
        "completed": False
    }

    tasks_db.append(new_task)
    return new_task


@router.get("/", response_model=List[TaskResponse])
def get_tasks():
    return tasks_db

