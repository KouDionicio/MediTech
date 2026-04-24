from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.usuario import get_usuario, get_usuario_by_email, get_usuarios, create_usuario, update_usuario, delete_usuario
from app.schemas.usuario import UsuarioCreate, UsuarioRead, UsuarioUpdate
from app.db.session import get_db

router = APIRouter()


@router.get("/", response_model=List[UsuarioRead])
def read_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_usuarios(db, skip=skip, limit=limit)


@router.get("/{usuario_id}", response_model=UsuarioRead)
def read_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = get_usuario(db, usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario


@router.post("/", response_model=UsuarioRead)
def create_new_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    existing = get_usuario_by_email(db, usuario.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email ya registrado")
    return create_usuario(db, usuario)


@router.put("/{usuario_id}", response_model=UsuarioRead)
def update_existing_usuario(usuario_id: int, usuario_update: UsuarioUpdate, db: Session = Depends(get_db)):
    updated = update_usuario(db, usuario_id, usuario_update)
    if updated is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return updated


@router.delete("/{usuario_id}")
def delete_existing_usuario(usuario_id: int, db: Session = Depends(get_db)):
    deleted = delete_usuario(db, usuario_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"success": True}
