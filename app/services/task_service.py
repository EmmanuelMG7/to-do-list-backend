"""
task_service.py

Este archivo contiene TODA la lógica de negocio relacionada con tareas.
No sabe nada de FastAPI, HTTP, ni rutas.
"""

from typing import List, Dict
from app.schemas.task import TaskCreate, TaskUpdate

# "Base de datos" temporal en memoria
# En el futuro esto será reemplazado por una base de datos real
tasks_db: List[Dict] = []

def create_task(task_data: TaskCreate) -> Dict:
    """
    Crea una nueva tarea y la guarda en la 'base de datos'.

    Parámetros:
    - task_data: esquema TaskCreate (datos validados por Pydantic)

    Retorna:
    - Diccionario representando la tarea creada
    """

    # Generamos un ID incremental simple
    new_task = {
        "id": len(tasks_db) + 1,
        "title": task_data.title,
        "description": task_data.description,
        "completed": False
    }

    # Guardamos la tarea
    tasks_db.append(new_task)

    return new_task

def get_all_tasks() -> List[Dict]:
    """
    Retorna todas las tareas existentes.
    """
    return tasks_db

def update_task(task_id: int, task_update: TaskUpdate) -> Dict:
    """
    Actualiza una tarea existente por su ID.

    Parámetros:
    - task_id: ID de la tarea a modificar
    - task_update: schema con campos opcionales a actualizar

    Retorna:
    - La tarea actualizada

    Lanza:
    - ValueError si la tarea no existe
    """

    for task in tasks_db:
        if task["id"] == task_id:

            # Convertimos el schema a dict
            # exclude_unset=True evita sobreescribir campos no enviados
            update_data = task_update.model_dump(exclude_unset=True)

            for key, value in update_data.items():
                task[key] = value

            return task

    # Si no encontramos la tarea
    raise ValueError("Task not found")

def delete_task(task_id: int) -> Dict:
    """
    Elimina una tarea por ID.

    Parámetros:
    - task_id: ID de la tarea a eliminar

    Retorna:
    - La tarea eliminada

    Lanza:
    - ValueError si la tarea no existe
    """

    for index, task in enumerate(tasks_db):
        if task["id"] == task_id:
            return tasks_db.pop(index)

    raise ValueError("Task not found")
