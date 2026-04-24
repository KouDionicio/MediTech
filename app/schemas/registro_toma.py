from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from app.models.registro_toma import EstadoToma, ConfirmadoPor


class RegistroTomaBase(BaseModel):
    horario_id: int
    dispositivo_id: Optional[int] = None
    fecha_hora_programada: datetime
    fecha_hora_toma: Optional[datetime] = None
    estado: EstadoToma = EstadoToma.PENDIENTE
    confirmado_por: Optional[ConfirmadoPor] = None


class RegistroTomaCreate(RegistroTomaBase):
    pass


class RegistroTomaUpdate(BaseModel):
    fecha_hora_toma: Optional[datetime] = None
    estado: Optional[EstadoToma] = None
    confirmado_por: Optional[ConfirmadoPor] = None


class RegistroTomaRead(RegistroTomaBase):
    id: int

    model_config = {"from_attributes": True}