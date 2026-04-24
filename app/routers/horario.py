from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.horario import get_horario, get_horarios_by_medicamento, get_horarios, create_horario, update_horario, delete_horario
from app.schemas.horario import HorarioCreate, HorarioRead, HorarioUpdate
from app.db.session import get_db

router = APIRouter()


@router.get("/", response_model=List[HorarioRead])
def read_horarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_horarios(db, skip=skip, limit=limit)


@router.get("/medicamento/{medicamento_id}", response_model=List[HorarioRead])
def read_horarios_by_medicamento(medicamento_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_horarios_by_medicamento(db, medicamento_id, skip=skip, limit=limit)


@router.get("/{horario_id}", response_model=HorarioRead)
def read_horario(horario_id: int, db: Session = Depends(get_db)):
    horario = get_horario(db, horario_id)
    if horario is None:
        raise HTTPException(status_code=404, detail="Horario no encontrado")
    return horario


@router.post("/", response_model=HorarioRead)
def create_new_horario(horario: HorarioCreate, db: Session = Depends(get_db)):
    return create_horario(db, horario)


@router.put("/{horario_id}", response_model=HorarioRead)
def update_existing_horario(horario_id: int, horario_update: HorarioUpdate, db: Session = Depends(get_db)):
    updated = update_horario(db, horario_id, horario_update)
    if updated is None:
        raise HTTPException(status_code=404, detail="Horario no encontrado")
    return updated


@router.delete("/{horario_id}")
def delete_existing_horario(horario_id: int, db: Session = Depends(get_db)):
    deleted = delete_horario(db, horario_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Horario no encontrado")
    return {"success": True}