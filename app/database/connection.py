"""
connection.py

Configura la conexión a la base de datos usando SQLAlchemy.
Define el engine, la sesión y la base declarativa ORM.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# =========================
# URL Base de datos
# =========================

DATABASE_URL = "sqlite:///./tasks.db"

# =========================
# Engine
# =========================

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # Necesario para SQLite con FastAPI
)

# =========================
# Sesión DB
# =========================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# =========================
# Base ORM
# =========================

Base = declarative_base()

