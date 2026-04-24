from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from app.models.dispositivo import EstadoDispositivo


class DispositivoBase(BaseModel):
    usuario_id: int
    mac_address: str
    nombre_dispositivo: Optional[str] = None
    estado: EstadoDispositivo = EstadoDispositivo.ACTIVO
    nivel_bateria: int = 100


class DispositivoCreate(DispositivoBase):
    pass


class DispositivoUpdate(BaseModel):
    nombre_dispositivo: Optional[str] = None
    estado: Optional[EstadoDispositivo] = None
    nivel_bateria: Optional[int] = None
    ultima_conexion: Optional[datetime] = None


class DispositivoRead(DispositivoBase):
    id: int
    ultima_conexion: Optional[datetime] = None
    fecha_registro: datetime

    model_config = {"from_attributes": True}