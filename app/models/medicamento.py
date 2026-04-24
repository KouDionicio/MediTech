from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Medicamento(Base):
    __tablename__ = "medicamentos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    nombre = Column(String(150), nullable=False)
    dosis = Column(String(50), nullable=False)
    presentacion = Column(String(100), nullable=False)
    cantidad_total = Column(Integer, nullable=False)
    stock_minimo = Column(Integer, default=5)
    estatus = Column(Boolean, default=True)

    usuario = relationship("Usuario", back_populates="medicamentos")
    horarios = relationship("Horario", back_populates="medicamento", cascade="all, delete-orphan")
