from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud.dispositivo import (
    get_dispositivo,
    get_dispositivo_by_mac,
    get_dispositivos,
    create_dispositivo,
    update_dispositivo,
    delete_dispositivo
)

from schemas.dispositivo import (
    DispositivoCreate,
    DispositivoRead,
    DispositivoUpdate
)

from db.session import get_db
from core.auth import get_current_user


router = APIRouter()


@router.get("/", response_model=List[DispositivoRead])
def read_dispositivos(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    return get_dispositivos(db, skip=skip, limit=limit)


@router.get("/{dispositivo_id}", response_model=DispositivoRead)
def read_dispositivo(
    dispositivo_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    dispositivo = get_dispositivo(db, dispositivo_id)
    if dispositivo is None:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    return dispositivo


@router.post("/", response_model=DispositivoRead)
def create_new_dispositivo(
    dispositivo: DispositivoCreate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    existing = get_dispositivo_by_mac(db, dispositivo.mac_address)
    if existing:
        raise HTTPException(status_code=400, detail="MAC address ya registrada")

    return create_dispositivo(db, dispositivo)


@router.put("/{dispositivo_id}", response_model=DispositivoRead)
def update_existing_dispositivo(
    dispositivo_id: int,
    dispositivo_update: DispositivoUpdate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    updated = update_dispositivo(db, dispositivo_id, dispositivo_update)
    if updated is None:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    return updated


@router.delete("/{dispositivo_id}")
def delete_existing_dispositivo(
    dispositivo_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    deleted = delete_dispositivo(db, dispositivo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    return {"success": True}