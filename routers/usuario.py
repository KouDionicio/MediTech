from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud.usuario import (
    get_usuario,
    get_usuario_by_email,
    get_usuarios,
    create_usuario,
    update_usuario,
    delete_usuario
)

from schemas.usuario import UsuarioCreate, UsuarioRead, UsuarioUpdate
from db.session import get_db

# 🔐 seguridad
from core.security import hash_password
from core.auth import get_current_user


router = APIRouter()


# 🔒 PROTEGIDO (requiere token)
@router.get("/", response_model=List[UsuarioRead])
def read_usuarios(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)   # <- PROTECCIÓN
):
    return get_usuarios(db, skip=skip, limit=limit)


# 🔒 PROTEGIDO
@router.get("/{usuario_id}", response_model=UsuarioRead)
def read_usuario(
    usuario_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    db_usuario = get_usuario(db, usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario


# ❗ REGISTRO (NO protegido)
@router.post("/", response_model=UsuarioRead)
def create_new_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):

    existing = get_usuario_by_email(db, usuario.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email ya registrado")

    # 🔐 HASH PASSWORD
    usuario.password = hash_password(usuario.password)

    return create_usuario(db, usuario)


# 🔒 PROTEGIDO
@router.put("/{usuario_id}", response_model=UsuarioRead)
def update_existing_usuario(
    usuario_id: int,
    usuario_update: UsuarioUpdate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    updated = update_usuario(db, usuario_id, usuario_update)
    if updated is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return updated


# 🔒 PROTEGIDO
@router.delete("/{usuario_id}")
def delete_existing_usuario(
    usuario_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    deleted = delete_usuario(db, usuario_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"success": True}