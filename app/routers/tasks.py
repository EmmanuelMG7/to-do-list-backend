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

    Parámetros:
    - task_id: ID de la tarea que se quiere actualizar (viene en la URL)
    - task_update: datos a actualizar (vienen en el body)
    """
    # 1️⃣ Buscar la tarea por ID
    for task in tasks_db:
        if task["id"] == task_id:

            # 2️⃣ Convertimos el schema a dict
            # exclude_unset=True asegura que SOLO se incluyan
            # los campos enviados por el usuario
            update_data = task_update.model_dump(exclude_unset=True)

            # 3️⃣ Actualizamos campo por campo
            for key, value in update_data.items():
                task[key] = value

                # 4️⃣ Devolvemos la tarea actualizada
            return task
            

    # 5️⃣ Si no se encontró la tarea, lanzamos error 404
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