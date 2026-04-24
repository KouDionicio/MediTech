from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud.registro_toma import (
    get_registro_toma,
    get_registros_toma_by_horario,
    get_registros_toma,
    create_registro_toma,
    update_registro_toma,
    delete_registro_toma
)

from schemas.registro_toma import (
    RegistroTomaCreate,
    RegistroTomaRead,
    RegistroTomaUpdate
)

from db.session import get_db
from core.auth import get_current_user


router = APIRouter()


@router.get("/", response_model=List[RegistroTomaRead])
def read_registros_toma(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    return get_registros_toma(db, skip=skip, limit=limit)


@router.get("/horario/{horario_id}", response_model=List[RegistroTomaRead])
def read_registros_toma_by_horario(
    horario_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    return get_registros_toma_by_horario(db, horario_id, skip=skip, limit=limit)


@router.get("/{registro_id}", response_model=RegistroTomaRead)
def read_registro_toma(
    registro_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    registro = get_registro_toma(db, registro_id)
    if registro is None:
        raise HTTPException(status_code=404, detail="Registro de toma no encontrado")
    return registro


@router.post("/", response_model=RegistroTomaRead)
def create_new_registro_toma(
    registro: RegistroTomaCreate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    return create_registro_toma(db, registro)


@router.put("/{registro_id}", response_model=RegistroTomaRead)
def update_existing_registro_toma(
    registro_id: int,
    registro_update: RegistroTomaUpdate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    updated = update_registro_toma(db, registro_id, registro_update)
    if updated is None:
        raise HTTPException(status_code=404, detail="Registro de toma no encontrado")
    return updated


@router.delete("/{registro_id}")
def delete_existing_registro_toma(
    registro_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    deleted = delete_registro_toma(db, registro_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Registro de toma no encontrado")
    return {"success": True}