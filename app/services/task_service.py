"""
task_service.py

Lógica de negocio desacoplada del tipo de repositorio.
"""

from typing import List, Dict
from app.schemas.task import TaskCreate, TaskUpdate
from app.repositories.task_repository import TaskRepository


# =========================
# Lógica de negocio
# =========================

def create_task(task_data: TaskCreate, repository: TaskRepository) -> Dict:
    """
    Crea una nueva tarea.
    """

    new_task = {
        "title": task_data.title,
        "description": task_data.description,
        "completed": False
    }

    return repository.create(new_task)


# -------------------------------------------------

def get_all_tasks(repository: TaskRepository) -> List[Dict]:
    return repository.get_all()


# -------------------------------------------------

def update_task(task_id: int, task_update: TaskUpdate, repository: TaskRepository) -> Dict:
    update_data = task_update.model_dump(exclude_unset=True)

    return repository.update(task_id, update_data)


# -------------------------------------------------

def delete_task(task_id: int, repository: TaskRepository) -> Dict:
    return repository.delete(task_id)