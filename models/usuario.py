import enum
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Enum as SQLEnum
from sqlalchemy.orm import relationship

from db.base import Base


class RolUsuario(str, enum.Enum):
    PACIENTE = "PACIENTE"
    CUIDADOR = "CUIDADOR"
    ADMIN = "ADMIN"


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True, index=True)
    telefono = Column(String(20), nullable=True)
    rol = Column(SQLEnum(RolUsuario), nullable=False, default=RolUsuario.PACIENTE)
    password = Column(String(255), nullable=False)
    fecha_registro = Column(DateTime, nullable=False, default=datetime.utcnow)

    dispositivos = relationship("Dispositivo", back_populates="usuario", cascade="all, delete-orphan")
    medicamentos = relationship("Medicamento", back_populates="usuario", cascade="all, delete-orphan")
    alertas = relationship("Alerta", back_populates="usuario", cascade="all, delete-orphan")
