"""
task_repository.py

Define el contrato que cualquier repositorio de tareas debe cumplir.
El objetivo es desacoplar la lógica de negocio del mecanismo de persistencia.
"""

from abc import ABC, abstractmethod
from typing import List, Dict

class TaskRepository(ABC):
    """
    Interfaz base para repositorios de tareas.
    """

    @abstractmethod
    def create(self, task: Dict) -> Dict:
        """
        Guarda una nueva tarea.
        """
        pass

    @abstractmethod
    def get_all(self) -> List[Dict]:
        """
        Retorna todas las tareas almacenadas.
        """
        pass

    @abstractmethod
    def update(self, task_id: int, update_data: Dict) -> Dict:
        """
        Actualiza una tarea existente.
        """
        pass

    @abstractmethod
    def delete(self, task_id: int) -> Dict:
        """
        Elimina una tarea existente.
        """
        pass