from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum as SQLEnum, ForeignKey, Text
from sqlalchemy.orm import relationship
from db.base import Base
import enum


class TipoAlerta(str, enum.Enum):
    TOMA_PENDIENTE = "TOMA_PENDIENTE"
    TOMA_OMITIDA = "TOMA_OMITIDA"
    STOCK_BAJO = "STOCK_BAJO"
    DISPOSITIVO_DESCONECTADO = "DISPOSITIVO_DESCONECTADO"


class Alerta(Base):
    __tablename__ = "alertas"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    tipo_alerta = Column(SQLEnum(TipoAlerta), nullable=False)
    mensaje = Column(Text, nullable=False)
    leida = Column(Boolean, default=False)
    fecha_alerta = Column(DateTime, nullable=False, default=datetime.utcnow)

    usuario = relationship("Usuario", back_populates="alertas")
