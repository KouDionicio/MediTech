from sqlalchemy.orm import Session
from app.models.horario import Horario
from app.schemas.horario import HorarioCreate, HorarioUpdate


def get_horario(db: Session, horario_id: int) -> Horario | None:
    return db.query(Horario).filter(Horario.id == horario_id).first()


def get_horarios_by_medicamento(db: Session, medicamento_id: int, skip: int = 0, limit: int = 100):
    return db.query(Horario).filter(Horario.medicamento_id == medicamento_id).offset(skip).limit(limit).all()


def get_horarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Horario).offset(skip).limit(limit).all()


def create_horario(db: Session, horario: HorarioCreate) -> Horario:
    db_horario = Horario(
        medicamento_id=horario.medicamento_id,
        dispositivo_id=horario.dispositivo_id,
        hora_toma=horario.hora_toma,
        dias_semana=horario.dias_semana,
        duracion_tratamiento=horario.duracion_tratamiento,
        fecha_inicio=horario.fecha_inicio,
        fecha_fin=horario.fecha_fin,
    )
    db.add(db_horario)
    db.commit()
    db.refresh(db_horario)
    return db_horario


def update_horario(db: Session, horario_id: int, update: HorarioUpdate) -> Horario | None:
    db_horario = get_horario(db, horario_id)
    if not db_horario:
        return None
    for field, value in update.model_dump(exclude_unset=True).items():
        setattr(db_horario, field, value)
    db.commit()
    db.refresh(db_horario)
    return db_horario


def delete_horario(db: Session, horario_id: int) -> bool:
    db_horario = get_horario(db, horario_id)
    if not db_horario:
        return False
    db.delete(db_horario)
    db.commit()
    return True
