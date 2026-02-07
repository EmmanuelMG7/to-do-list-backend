"""
json_task_repository.py

Implementación del repositorio de tareas utilizando un archivo JSON
como mecanismo de persistencia.
"""

import json
from pathlib import Path
from typing import List, Dict

from app.repositories.task_repository import TaskRepository


class JsonTaskRepository(TaskRepository):
    """
    Implementación concreta del repositorio de tareas
    usando almacenamiento en archivo JSON.
    """

    DATA_FILE = Path("data/tasks.json")

    # =========================
    # Persistencia interna
    # =========================

    def _load_tasks(self) -> List[Dict]:
        """
        Carga las tareas desde el archivo JSON.
        """
        if not self.DATA_FILE.exists():
            return []

        with open(self.DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    def _save_tasks(self, tasks: List[Dict]) -> None:
        """
        Guarda las tareas en el archivo JSON.
        """
        self.DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

        with open(self.DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)

    # =========================
    # Implementación del contrato
    # =========================

    def create(self, task: Dict) -> Dict:
        tasks = self._load_tasks()
        tasks.append(task)
        self._save_tasks(tasks)
        return task

    def get_all(self) -> List[Dict]:
        return self._load_tasks()

    def update(self, task_id: int, update_data: Dict) -> Dict:
        tasks = self._load_tasks()

        for task in tasks:
            if task["id"] == task_id:
                task.update(update_data)
                self._save_tasks(tasks)
                return task

        raise ValueError("Task not found")

    def delete(self, task_id: int) -> Dict:
        tasks = self._load_tasks()

        for index, task in enumerate(tasks):
            if task["id"] == task_id:
                deleted_task = tasks.pop(index)
                self._save_tasks(tasks)
                return deleted_task

        raise ValueError("Task not found")
