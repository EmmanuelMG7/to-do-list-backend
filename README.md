# To-Do List Backend API

## Descripción

Backend API REST para la gestión de tareas (To-Do List), desarrollada con **Python y FastAPI**.

Este proyecto fue construido siguiendo la metodología **Scrum**, simulando un entorno profesional de desarrollo con sprints, backlog y documentación técnica.

---

## Tecnologías

* Python
* FastAPI
* SQLite
* SQLAlchemy (ORM)
* Pydantic (validaciones)
* Git & GitHub

---

## Arquitectura

El proyecto está organizado siguiendo una arquitectura por capas:

* **Routers** → Manejan las requests HTTP
* **Services** → Contienen la lógica de negocio
* **Repositories** → Gestionan la persistencia de datos
* **Models (ORM)** → Definen la estructura de la base de datos
* **Schemas (Pydantic)** → Validan entrada y salida de datos

Se implementa el patrón **Repository**, lo que permite cambiar fácilmente el motor de base de datos sin afectar la lógica del sistema.

---

## Funcionalidades

* Crear tareas
* Listar tareas
* Actualizar tareas (parcial o completo)
* Eliminar tareas

---

## Validaciones

* El título es obligatorio
* El título debe tener al menos 3 caracteres
* No se permiten valores vacíos o solo espacios
* La descripción es opcional pero válida si se envía
* No se permiten campos adicionales en las requests (`extra = forbid`)
* Manejo de errores HTTP (404, 422)

---

## Documentación interactiva

Disponible en:

```
http://127.0.0.1:8000/docs
```

---

## Endpoints principales

| Método | Endpoint           | Descripción      |
| ------ | ------------------ | ---------------- |
| POST   | /api/v1/tasks      | Crear tarea      |
| GET    | /api/v1/tasks      | Listar tareas    |
| PUT    | /api/v1/tasks/{id} | Actualizar tarea |
| DELETE | /api/v1/tasks/{id} | Eliminar tarea   |

---

## Futuras mejoras

* Migración a PostgreSQL
* Implementación de autenticación (JWT)
* Uso de Alembic para migraciones de base de datos
* Dockerización del proyecto

---

## Estructura del proyecto

```
app/
├── routers/
├── services/
├── repositories/
├── models/
├── schemas/
├── database/
└── main.py
```

---

## Autor

Proyecto desarrollado como parte de portafolio backend por Emmanuel Mora Grajales
