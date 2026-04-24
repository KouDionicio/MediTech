from pydantic import BaseModel
from typing import Optional


class MedicamentoBase(BaseModel):
    usuario_id: int
    nombre: str
    dosis: str
    presentacion: str
    cantidad_total: int
    stock_minimo: int = 5
    estatus: bool = True


class MedicamentoCreate(MedicamentoBase):
    pass


class MedicamentoUpdate(BaseModel):
    nombre: Optional[str] = None
    dosis: Optional[str] = None
    presentacion: Optional[str] = None
    cantidad_total: Optional[int] = None
    stock_minimo: Optional[int] = None
    estatus: Optional[bool] = None


class MedicamentoRead(MedicamentoBase):
    id: int

    model_config = {"from_attributes": True}