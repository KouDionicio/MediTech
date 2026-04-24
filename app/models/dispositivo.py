from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from app.db.base import Base
import enum


class EstadoDispositivo(str, enum.Enum):
    ACTIVO = "ACTIVO"
    INACTIVO = "INACTIVO"
    MANTENIMIENTO = "MANTENIMIENTO"


class Dispositivo(Base):
    __tablename__ = "dispositivos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    mac_address = Column(String(17), nullable=False, unique=True, index=True)
    nombre_dispositivo = Column(String(100), nullable=True)
    estado = Column(SQLEnum(EstadoDispositivo), nullable=False, default=EstadoDispositivo.ACTIVO)
    nivel_bateria = Column(Integer, default=100)
    ultima_conexion = Column(DateTime, nullable=True)
    fecha_registro = Column(DateTime, nullable=False)

    usuario = relationship("Usuario", back_populates="dispositivos")
    horarios = relationship("Horario", back_populates="dispositivo")
    registros_toma = relationship("RegistroToma", back_populates="dispositivo")
