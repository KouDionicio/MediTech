from sqlalchemy import Column, Integer, DateTime, Enum as SQLEnum, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
import enum


class EstadoToma(str, enum.Enum):
    TOMADO = "TOMADO"
    OMITIDO = "OMITIDO"
    PENDIENTE = "PENDIENTE"


class ConfirmadoPor(str, enum.Enum):
    USUARIO = "USUARIO"
    SENSOR = "SENSOR"
    CUIDADOR = "CUIDADOR"


class RegistroToma(Base):
    __tablename__ = "registros_toma"

    id = Column(Integer, primary_key=True, index=True)
    horario_id = Column(Integer, ForeignKey("horarios.id"), nullable=False)
    dispositivo_id = Column(Integer, ForeignKey("dispositivos.id"), nullable=True)
    fecha_hora_programada = Column(DateTime, nullable=False)
    fecha_hora_toma = Column(DateTime, nullable=True)
    estado = Column(SQLEnum(EstadoToma), nullable=False, default=EstadoToma.PENDIENTE)
    confirmado_por = Column(SQLEnum(ConfirmadoPor), nullable=True)

    horario = relationship("Horario", back_populates="registros_toma")
    dispositivo = relationship("Dispositivo", back_populates="registros_toma")