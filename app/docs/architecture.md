# Arquitectura del Proyecto

## Descripción general

El proyecto sigue una arquitectura por capas que separa responsabilidades para facilitar el mantenimiento, escalabilidad y testeo.

---

## Capas del sistema

### 1. Routers

Responsables de manejar las solicitudes HTTP.

* Reciben requests
* Llaman a los services
* Retornan respuestas
* Manejan errores HTTP

---

### 2. Services

Contienen la lógica de negocio.

* Procesan datos
* Aplican reglas de negocio
* No conocen detalles de persistencia

---

### 3. Repositories

Encargados de la persistencia.

* Implementan el acceso a datos
* Pueden cambiar sin afectar el resto del sistema

---

### 4. Models (ORM)

Definen la estructura de la base de datos usando SQLAlchemy.

---

### 5. Schemas (Pydantic)

Validan los datos de entrada y salida.

---

## 🔄 Flujo de datos

Request → Router → Service → Repository → DB → Response

---

## Decisión clave

Se implementó el patrón Repository para desacoplar la lógica de negocio del acceso a datos, permitiendo cambiar fácilmente el motor de base de datos.
