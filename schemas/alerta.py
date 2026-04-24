from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from models.alerta import TipoAlerta


class AlertaBase(BaseModel):
    usuario_id: int
    tipo_alerta: TipoAlerta
    mensaje: str
    leida: bool = False


class AlertaCreate(AlertaBase):
    pass


class AlertaUpdate(BaseModel):
    mensaje: Optional[str] = None
    leida: Optional[bool] = None


class AlertaRead(AlertaBase):
    id: int
    fecha_alerta: datetime

    model_config = {"from_attributes": True}
