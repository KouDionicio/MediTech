from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.dispositivo import get_dispositivo, get_dispositivo_by_mac, get_dispositivos, create_dispositivo, update_dispositivo, delete_dispositivo
from app.schemas.dispositivo import DispositivoCreate, DispositivoRead, DispositivoUpdate
from app.db.session import get_db

router = APIRouter()


@router.get("/", response_model=List[DispositivoRead])
def read_dispositivos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_dispositivos(db, skip=skip, limit=limit)


@router.get("/{dispositivo_id}", response_model=DispositivoRead)
def read_dispositivo(dispositivo_id: int, db: Session = Depends(get_db)):
    dispositivo = get_dispositivo(db, dispositivo_id)
    if dispositivo is None:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    return dispositivo


@router.post("/", response_model=DispositivoRead)
def create_new_dispositivo(dispositivo: DispositivoCreate, db: Session = Depends(get_db)):
    existing = get_dispositivo_by_mac(db, dispositivo.mac_address)
    if existing:
        raise HTTPException(status_code=400, detail="MAC address ya registrada")
    return create_dispositivo(db, dispositivo)


@router.put("/{dispositivo_id}", response_model=DispositivoRead)
def update_existing_dispositivo(dispositivo_id: int, dispositivo_update: DispositivoUpdate, db: Session = Depends(get_db)):
    updated = update_dispositivo(db, dispositivo_id, dispositivo_update)
    if updated is None:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    return updated


@router.delete("/{dispositivo_id}")
def delete_existing_dispositivo(dispositivo_id: int, db: Session = Depends(get_db)):
    deleted = delete_dispositivo(db, dispositivo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    return {"success": True}
