"""
task_service.py

Este archivo contiene TODA la lógica de negocio relacionada con tareas.
No sabe nada de FastAPI, HTTP, ni rutas.
"""

from typing import List, Dict
from app.schemas.task import TaskCreate, TaskUpdate
from app.repositories.json_task_repository import JsonTaskRepository

# Instancia del repository
repository = JsonTaskRepository()

# =========================
# Lógica de negocio
# =========================

def create_task(task_data: TaskCreate) -> Dict:
    tasks = repository.get_all()

    new_id = max([task["id"] for task in tasks], default=0) + 1

    new_task = {
        "id": new_id,
        "title": task_data.title,
        "description": task_data.description,
        "completed": False
    }

    return repository.create(new_task)

# -------------------------------------------------

def get_all_tasks() -> List[Dict]:
    return repository.get_all()

# -------------------------------------------------

def update_task(task_id: int, task_update: TaskUpdate) -> Dict:
    update_data = task_update.model_dump(exclude_unset=True)

    return repository.update(task_id, update_data)


# -------------------------------------------------

def delete_task(task_id: int) -> Dict:
    return repository.delete(task_id)



