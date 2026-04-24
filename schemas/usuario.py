from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

from models.usuario import RolUsuario


class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr
    telefono: Optional[str] = None
    rol: RolUsuario = RolUsuario.PACIENTE


class UsuarioCreate(UsuarioBase):
    password: str


class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    telefono: Optional[str] = None
    rol: Optional[RolUsuario] = None


class UsuarioRead(UsuarioBase):
    id: int
    fecha_registro: datetime

    model_config = {"from_attributes": True}
