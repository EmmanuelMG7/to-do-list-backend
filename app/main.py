from fastapi import FastAPI

from app.routers import health, tasks

from app.models.task_model import Task


app = FastAPI(
    title="To-Do List Backend",
    description="Backend API para una aplicación de To-Do List",
    version="1.0.0"
)

# Registrar routers
app.include_router(health.router)
app.include_router(tasks.router)
