# Decisiones Técnicas

## Uso de FastAPI

Se eligió FastAPI por su rapidez, soporte para tipado y documentación automática con Swagger.

---

## Uso de SQLAlchemy

Permite trabajar con la base de datos mediante ORM, evitando escribir SQL manual y facilitando la escalabilidad.

---

## Patrón Repository

Se implementó para desacoplar la lógica de negocio de la persistencia.

Esto permite cambiar de JSON a SQLAlchemy sin afectar el resto del sistema.

---

## Separación por capas

Se separó el proyecto en routers, services y repositories para mejorar la mantenibilidad y claridad del código.

---

## Uso de Pydantic

Se utiliza para validar datos de entrada y salida, asegurando integridad y evitando errores.

---

## SQLite como base inicial

Se eligió SQLite por simplicidad en desarrollo, con intención de migrar a otros motores de Bases de Datos en el futuro.
