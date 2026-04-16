# API Endpoints

## Base URL

/api/v1

---

## Crear tarea

POST /tasks

### Request

```json
{
  "title": "*titulo*",
  "description": "*descripcion*"
}
```

### Response

```json
{
  "id": 1,
  "title": "*titulo*",
  "description": "*descripcion*",
  "completed": false
}
```

El ID se genera automaticamente.

---

## Obtener tareas

GET /tasks

---

## Actualizar tarea

PUT /tasks/{id}

---

## Eliminar tarea

DELETE /tasks/{id}

---

## Errores

* 404 → Task not found
* 422 → Error de validación
