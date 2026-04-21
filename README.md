# To-Do List Backend API

## Description

A RESTful backend API for managing tasks (To-Do List), built with **Python and FastAPI**, applying clean architecture principles and the **Repository Pattern** to decouple business logic from data persistence.

This project was developed following the **Scrum methodology**, simulating a real-world professional development environment with sprints, backlog, and technical documentation.

---

## Tech Stack

* Python
* FastAPI
* SQLite
* SQLAlchemy (ORM)
* Pydantic (data validation)
* Git & GitHub

---

## Architecture

The project follows a layered architecture:

* **Routers** → Handle HTTP requests and responses
* **Services** → Contain business logic
* **Repositories** → Manage data persistence
* **Models (ORM)** → Define database structure using SQLAlchemy
* **Schemas (Pydantic)** → Validate input and output data

The **Repository Pattern** is implemented to ensure the system is easily extendable and database-agnostic.

---

## Features

* Create tasks
* Retrieve all tasks
* Update tasks (partial or full updates)
* Delete tasks

---

## Validation Rules

* Title is required
* Title must be at least 3 characters long
* Empty or whitespace-only values are not allowed
* Description is optional but must be valid if provided
* Extra fields are forbidden (`extra = forbid`)
* Proper HTTP error handling (404, 422)

---

## Interactive API Docs

Available at:

```text
http://127.0.0.1:8000/docs
```

---

## Main Endpoints

| Method | Endpoint           | Description   |
| ------ | ------------------ | ------------- |
| POST   | /api/v1/tasks      | Create a task |
| GET    | /api/v1/tasks      | Get all tasks |
| PUT    | /api/v1/tasks/{id} | Update a task |
| DELETE | /api/v1/tasks/{id} | Delete a task |

---

## Future Improvements

* Migration to PostgreSQL
* JWT Authentication
* Database migrations with Alembic
* Dockerization

---

## Project Structure

```text
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

## Author

Developed as part of a backend portfolio project by Emmanuel Mora Grajales
