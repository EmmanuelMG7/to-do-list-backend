from fastapi import APIRouter, HTTPException
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from typing import List
from app.services.task_service import ( 
    create_task as create_task_service, 
    get_all_tasks, 
    update_task as update_task_service,
    delete_task as delete_task_service 
)

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.repositories.sqlalchemy_task_repository import SQLAlchemyTaskRepository
#################################################################

router = APIRouter(
    prefix="/api/v1/tasks",
    tags=["Tasks"]
)
#################################################################

@router.post("/", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    repository = SQLAlchemyTaskRepository(db)
    new_task = create_task_service(task, repository)
    return new_task

#################################################################

@router.get("/", response_model=List[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    repository = SQLAlchemyTaskRepository(db)
    return get_all_tasks(repository)

#################################################################

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    db: Session = Depends(get_db)
):
    repository = SQLAlchemyTaskRepository(db)

    try:
        return update_task_service(task_id, task_update, repository)
    except ValueError:
        raise HTTPException(status_code=404, detail="Task not found")

#################################################################

@router.delete("/{task_id}", response_model=TaskResponse)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    repository = SQLAlchemyTaskRepository(db)

    try:
        return delete_task_service(task_id, repository)
    except ValueError:
        raise HTTPException(status_code=404, detail="Task not found")