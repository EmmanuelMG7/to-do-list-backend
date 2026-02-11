"""
task_model.py

Define el modelo ORM Task para SQLAlchemy.
Representa la tabla tasks en la base de datos.
"""

from sqlalchemy import Column, Integer, String, Boolean
from app.database.connection import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
