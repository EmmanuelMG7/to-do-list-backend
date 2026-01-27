from pydantic import BaseModel, field_validator
from typing import Optional

class TaskCreate(BaseModel):
    """
    Schema utilizado para CREAR una nueva tarea.

    Este schema se encarga de:
    - Validar los datos que el cliente envía
    - Evitar que entren datos inválidos al sistema
    """

    title: str
    description: Optional[str] = None

    #Validador de 'title' 

    @field_validator("title")
    @classmethod

    def validate_title(cls, value: str) -> str:
        """
        Valida el campo 'title'.

        Se ejecuta automáticamente cada vez que:
        - Se intenta crear una TaskCreate
        - FastAPI recibe un request POST /tasks

        Reglas:
        - No puede estar vacío
        - No puede ser solo espacios
        - Debe tener al menos 3 caracteres
        """
        # Eliminamos espacios al inicio y al final
        cleaned_value = value.strip()

        # Validamos que no esté vacío
        if not cleaned_value:
            raise ValueError("Title cannot be empty")

        # Validamos longitud mínima
        if len(cleaned_value) < 3:
            raise ValueError("Title must have at least 3 characters")

        # Retornamos el valor limpio
        return cleaned_value

     #Validador de 'description'   

    @field_validator("description")
    @classmethod
    def validate_description(cls, value: Optional[str]) -> Optional[str]:
        """
        Valida el campo 'description'.

        - Es opcional
        - Pero si viene, no puede ser solo espacios
        """

        # Si no viene description, no validamos nada
        if value is None:
            return value

        # Eliminamos espacios
        cleaned_value = value.strip()

        # Si queda vacío, es inválido
        if not cleaned_value:
            raise ValueError("Description cannot be empty if provided")

        return cleaned_value


 #################################################################   

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool

#################################################################   

class TaskUpdate(BaseModel):
    """
    Schema utilizado para ACTUALIZAR una tarea existente.

    - Todos los campos son opcionales
    - Solo se validan los campos que el usuario envía
    """

    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

    @field_validator("title")
    @classmethod

     #Validador de 'title'   

    def validate_title(cls, value: Optional[str]) -> Optional[str]:
        """
        Valida el título SOLO si fue enviado.

        Reglas:
        - No puede estar vacío
        - No puede ser solo espacios
        - Debe tener al menos 3 caracteres
        """

        # Si no se envió title, no validamos nada
        if value is None:
            return value

        cleaned_value = value.strip()

        if not cleaned_value:
            raise ValueError("Title cannot be empty")

        if len(cleaned_value) < 3:
            raise ValueError("Title must have at least 3 characters")

        return cleaned_value
    
    
     #Validador de 'description'   

    @field_validator("description")
    @classmethod
    def validate_description(cls, value: Optional[str]) -> Optional[str]:
        """
        Valida la descripción SOLO si fue enviada.
        """

        if value is None:
            return value

        cleaned_value = value.strip()

        if not cleaned_value:
            raise ValueError("Description cannot be empty if provided")

        return cleaned_value

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

#################################################################   
