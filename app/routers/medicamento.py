from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.medicamento import get_medicamento, get_medicamentos_by_usuario, get_medicamentos, create_medicamento, update_medicamento, delete_medicamento
from app.schemas.medicamento import MedicamentoCreate, MedicamentoRead, MedicamentoUpdate
from app.db.session import get_db

router = APIRouter()


@router.get("/", response_model=List[MedicamentoRead])
def read_medicamentos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_medicamentos(db, skip=skip, limit=limit)


@router.get("/usuario/{usuario_id}", response_model=List[MedicamentoRead])
def read_medicamentos_by_usuario(usuario_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_medicamentos_by_usuario(db, usuario_id, skip=skip, limit=limit)


@router.get("/{medicamento_id}", response_model=MedicamentoRead)
def read_medicamento(medicamento_id: int, db: Session = Depends(get_db)):
    medicamento = get_medicamento(db, medicamento_id)
    if medicamento is None:
        raise HTTPException(status_code=404, detail="Medicamento no encontrado")
    return medicamento


@router.post("/", response_model=MedicamentoRead)
def create_new_medicamento(medicamento: MedicamentoCreate, db: Session = Depends(get_db)):
    return create_medicamento(db, medicamento)


@router.put("/{medicamento_id}", response_model=MedicamentoRead)
def update_existing_medicamento(medicamento_id: int, medicamento_update: MedicamentoUpdate, db: Session = Depends(get_db)):
    updated = update_medicamento(db, medicamento_id, medicamento_update)
    if updated is None:
        raise HTTPException(status_code=404, detail="Medicamento no encontrado")
    return updated


@router.delete("/{medicamento_id}")
def delete_existing_medicamento(medicamento_id: int, db: Session = Depends(get_db)):
    deleted = delete_medicamento(db, medicamento_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Medicamento no encontrado")
    return {"success": True}