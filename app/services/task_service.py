"""
task_service.py

Este archivo contiene TODA la lógica de negocio relacionada con tareas.
No sabe nada de FastAPI, HTTP, ni rutas.
"""

from typing import List, Dict
from app.schemas.task import TaskCreate, TaskUpdate
import json
from pathlib import Path

# Ruta del archivo de persistencia
DATA_FILE = Path("data/tasks.json")

# =========================
# Persistencia
# =========================

def load_tasks() -> List[Dict]:
    """
    Carga las tareas desde el archivo JSON.
    Si el archivo no existe, retorna una lista vacía.
    """
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks: List[Dict]) -> None:
    """
    Guarda la lista completa de tareas en el archivo JSON.
    """
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)


#################################################################


# =========================
# Lógica de negocio
# =========================

# "Base de datos" temporal en memoria
# En el futuro esto será reemplazado por una base de datos real

#################################################################

tasks_db: List[Dict] = []

def create_task(task_data: TaskCreate) -> Dict:
    tasks_db = load_tasks()

    new_task = {
        "id": len(tasks_db) + 1,
        "title": task_data.title,
        "description": task_data.description,
        "completed": False
    }

    tasks_db.append(new_task)
    save_tasks(tasks_db)

    return new_task

#################################################################


def get_all_tasks() -> List[Dict]:
    return load_tasks()

#################################################################

def update_task(task_id: int, task_update: TaskUpdate) -> Dict:
    tasks_db = load_tasks()

    for task in tasks_db:
        if task["id"] == task_id:
            update_data = task_update.model_dump(exclude_unset=True)

            for key, value in update_data.items():
                task[key] = value

            save_tasks(tasks_db)
            return task

    raise ValueError("Task not found")

#################################################################

def delete_task(task_id: int) -> Dict:
    tasks_db = load_tasks()

    for index, task in enumerate(tasks_db):
        if task["id"] == task_id:
            deleted_task = tasks_db.pop(index)
            save_tasks(tasks_db)
            return deleted_task

    raise ValueError("Task not found")
