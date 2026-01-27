from fastapi import APIRouter, HTTPException
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from typing import List


tasks_db = []

#################################################################

router = APIRouter(
    prefix="/api/v1/tasks",
    tags=["Tasks"]
)
#################################################################

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

#################################################################

@router.get("/", response_model=List[TaskResponse])
def get_tasks():
    return tasks_db

#################################################################

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate):
    """
    Endpoint para actualizar una tarea existente.

    Reglas de negocio:
    - La tarea debe existir
    - El body NO puede estar vacío
    """

    # Convertimos el schema en un diccionario
    # exclude_unset=True:
    # - solo incluye los campos enviados por el cliente
    update_data = task_update.model_dump(exclude_unset=True)

    # Validación de negocio:
    # Si el cliente no envió ningún campo → error 400
    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="At least one field must be provided to update the task"
        )

    # Buscamos la tarea por ID
    for task in tasks_db:
        if task["id"] == task_id:

            # Actualizamos SOLO los campos enviados
            for key, value in update_data.items():
                task[key] = value

            # Retornamos la tarea actualizada
            return task

    # Si no se encuentra la tarea → 404
    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )

#################################################################

@router.delete("/tasks/{task_id}", response_model=TaskResponse)
def delete_task(task_id: int):
    """
    Endpoint para eliminar una tarea existente.

    Parámetros:
    - task_id: ID de la tarea a eliminar (viene desde la URL)

    Respuesta:
    - Devuelve la tarea eliminada si existe
    - Error 404 si no se encuentra la tarea
    """

    # Recorremos la lista de tareas simulando una "base de datos"
    for index, task in enumerate(tasks_db):
        # Comparamos el ID de cada tarea con el ID recibido
        if task["id"] == task_id:

            # Guardamos la tarea antes de eliminarla
            deleted_task = task

            # Eliminamos la tarea de la lista usando su índice
            tasks_db.pop(index)

            # Devolvemos la tarea eliminada
            return deleted_task

    # Si el bucle termina y no se encontró la tarea,
    # significa que el ID no existe → error 404
    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )