"""
sqlalchemy_task_repository.py

Repositorio que implementa persistencia usando SQLAlchemy.
"""

from typing import List, Dict
from sqlalchemy.orm import Session

from app.repositories.task_repository import TaskRepository
from app.models.task_model import Task


class SQLAlchemyTaskRepository(TaskRepository):

    def __init__(self, db: Session):
        self.db = db


    def create(self, task_data: Dict) -> Dict:
        new_task = Task(**task_data)

        self.db.add(new_task)
        self.db.commit()
        self.db.refresh(new_task)

        return self._to_dict(new_task)
    
    def get_all(self) -> List[Dict]:
        tasks = self.db.query(Task).all()
        return [self._to_dict(task) for task in tasks]
    
    def update(self, task_id: int, update_data: Dict) -> Dict:
        task = self.db.query(Task).filter(Task.id == task_id).first()

        if not task:
            raise ValueError("Task not found")

        for key, value in update_data.items():
            setattr(task, key, value)

        self.db.commit()
        self.db.refresh(task)

        return self._to_dict(task)
    
    def delete(self, task_id: int) -> Dict:
        task = self.db.query(Task).filter(Task.id == task_id).first()

        if not task:
            raise ValueError("Task not found")

        self.db.delete(task)
        self.db.commit()

        return {"message": "Task deleted"}
    
    def _to_dict(self, task: Task) -> Dict:
        return {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "completed": task.completed
        }



