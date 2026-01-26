from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

    class Config:
        """
        Configuración interna de Pydantic.
        """

        extra = "forbid"
        # extra = "forbid":
        # - Prohíbe campos que no estén definidos en el schema
        # - Si el usuario manda algo como:
        #   { "foo": "bar" }
        #   → FastAPI devuelve error 400 automáticamente
