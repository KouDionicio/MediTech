from datetime import date, time
from pydantic import BaseModel
from typing import Optional


class HorarioBase(BaseModel):
    medicamento_id: int
    dispositivo_id: Optional[int] = None
    hora_toma: time
    dias_semana: str
    duracion_tratamiento: Optional[int] = None
    fecha_inicio: date
    fecha_fin: Optional[date] = None


class HorarioCreate(HorarioBase):
    pass


class HorarioUpdate(BaseModel):
    hora_toma: Optional[time] = None
    dias_semana: Optional[str] = None
    duracion_tratamiento: Optional[int] = None
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None


class HorarioRead(HorarioBase):
    id: int

    model_config = {"from_attributes": True}
