# To-Do List Backend

Descripción: Backend API REST para gestionar tareas (To-Do List), desarrollado en Python utilizando FastAPI, siguiendo la metodología Scrum como proyecto de portfolio.

Metodología: Este proyecto se desarrolla aplicando Scrum, documentando sprints, backlog y retrospectivas para simular un entorno profesional real.

Stack Tecnológico:

-Python
-FastAPI
-SQLite
-SQLAlchemy
-Git & GitHub

Estado del proyecto: En Desarrollo


##  Funcionalidades

- Crear tareas (POST /api/v1/tasks)
- Listar tareas (GET /api/v1/tasks)
- Actualizar tareas (PUT /api/v1/tasks/{id})
- Eliminar tareas (DELETE /api/v1/tasks/{id})

##  Validaciones

- El título es obligatorio y debe tener al menos 3 caracteres
- No se permiten campos vacíos o inválidos
- No se permiten actualizaciones sin datos
- Manejo de errores 400, 404 y 422

##  Documentación interactiva

- Swagger UI disponible en: `/docs`

