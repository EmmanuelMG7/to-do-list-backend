from fastapi import APIRouter, HTTPException
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from typing import List
from app.services.task_service import ( 
    create_task as create_task_service, 
    get_all_tasks, 
    update_task as update_task_service,
    delete_task as delete_task_service 
)

#################################################################

router = APIRouter(
    prefix="/api/v1/tasks",
    tags=["Tasks"]
)
#################################################################

@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate):
    """
    Endpoint HTTP para crear una tarea.

    Responsabilidad:
    - Recibir la request
    - Llamar al service
    - Devolver la respuesta
    """

    # Delegamos la lógica de negocio al service
    new_task = create_task_service(task)

    # El router solo devuelve la respuesta
    return new_task

#################################################################

@router.get("/", response_model=List[TaskResponse])
def get_tasks():
    """
    Endpoint HTTP para listar todas las tareas.

    Responsabilidad:
    - Llamar al service
    - Retornar la lista de tareas
    """

    tasks = get_all_tasks()
    return tasks

#################################################################

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate):
    """
    Endpoint HTTP para actualizar una tarea existente.

    Responsabilidades del router:
    - Recibir parámetros HTTP
    - Llamar al service
    - Traducir errores de negocio a errores HTTP
    """

    try:
        # Delegamos TODA la lógica de actualización al service
        updated_task = update_task_service(task_id, task_update)

        # Si todo salió bien, devolvemos la tarea actualizada
        return updated_task

    except ValueError:
        # El service NO encontró la tarea
        # El router traduce ese error a HTTP 404
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

#################################################################

@router.delete("/{task_id}", response_model=TaskResponse)
def delete_task(task_id: int):
    """
    Endpoint HTTP para eliminar una tarea.

    Responsabilidades del router:
    - Recibir el ID desde la URL
    - Llamar al service
    - Traducir errores de negocio a HTTP
    """

    try:
        # Delegamos el borrado al service
        deleted_task = delete_task_service(task_id)

        # Retornamos la tarea eliminada
        return deleted_task

    except ValueError:
        # Si el service no encuentra la tarea
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )