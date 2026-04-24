from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Horario(Base):
    __tablename__ = "horarios"

    id = Column(Integer, primary_key=True, index=True)
    medicamento_id = Column(Integer, ForeignKey("medicamentos.id"), nullable=False)
    dispositivo_id = Column(Integer, ForeignKey("dispositivos.id"), nullable=True)
    hora_toma = Column(Time, nullable=False)
    dias_semana = Column(String(50), nullable=False)
    duracion_tratamiento = Column(Integer, nullable=True)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=True)

    medicamento = relationship("Medicamento", back_populates="horarios")
    dispositivo = relationship("Dispositivo", back_populates="horarios")
    registros_toma = relationship("RegistroToma", back_populates="horario", cascade="all, delete-orphan")
