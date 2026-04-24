from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud.alerta import (
    get_alerta,
    get_alertas_by_usuario,
    get_alertas,
    create_alerta,
    update_alerta,
    delete_alerta
)

from schemas.alerta import (
    AlertaCreate,
    AlertaRead,
    AlertaUpdate
)

from db.session import get_db
from core.auth import get_current_user


router = APIRouter()


@router.get("/", response_model=List[AlertaRead])
def read_alertas(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    return get_alertas(db, skip=skip, limit=limit)


@router.get("/usuario/{usuario_id}", response_model=List[AlertaRead])
def read_alertas_by_usuario(
    usuario_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    return get_alertas_by_usuario(db, usuario_id, skip=skip, limit=limit)


@router.get("/{alerta_id}", response_model=AlertaRead)
def read_alerta(
    alerta_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    alerta = get_alerta(db, alerta_id)
    if alerta is None:
        raise HTTPException(status_code=404, detail="Alerta no encontrada")
    return alerta


@router.post("/", response_model=AlertaRead)
def create_new_alerta(
    alerta: AlertaCreate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    return create_alerta(db, alerta)


@router.put("/{alerta_id}", response_model=AlertaRead)
def update_existing_alerta(
    alerta_id: int,
    alerta_update: AlertaUpdate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    updated = update_alerta(db, alerta_id, alerta_update)
    if updated is None:
        raise HTTPException(status_code=404, detail="Alerta no encontrada")
    return updated


@router.delete("/{alerta_id}")
def delete_existing_alerta(
    alerta_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    deleted = delete_alerta(db, alerta_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Alerta no encontrada")
    return {"success": True}