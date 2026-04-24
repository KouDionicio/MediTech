from sqlalchemy.orm import Session
from models.registro_toma import RegistroToma
from schemas.registro_toma import RegistroTomaCreate, RegistroTomaUpdate


def get_registro_toma(db: Session, registro_id: int) -> RegistroToma | None:
    return db.query(RegistroToma).filter(RegistroToma.id == registro_id).first()


def get_registros_toma_by_horario(db: Session, horario_id: int, skip: int = 0, limit: int = 100):
    return db.query(RegistroToma).filter(RegistroToma.horario_id == horario_id).offset(skip).limit(limit).all()


def get_registros_toma(db: Session, skip: int = 0, limit: int = 100):
    return db.query(RegistroToma).offset(skip).limit(limit).all()


def create_registro_toma(db: Session, registro: RegistroTomaCreate) -> RegistroToma:
    db_registro = RegistroToma(
        horario_id=registro.horario_id,
        dispositivo_id=registro.dispositivo_id,
        fecha_hora_programada=registro.fecha_hora_programada,
        fecha_hora_toma=registro.fecha_hora_toma,
        estado=registro.estado,
        confirmado_por=registro.confirmado_por,
    )
    db.add(db_registro)
    db.commit()
    db.refresh(db_registro)
    return db_registro


def update_registro_toma(db: Session, registro_id: int, update: RegistroTomaUpdate) -> RegistroToma | None:
    db_registro = get_registro_toma(db, registro_id)
    if not db_registro:
        return None
    for field, value in update.model_dump(exclude_unset=True).items():
        setattr(db_registro, field, value)
    db.commit()
    db.refresh(db_registro)
    return db_registro


def delete_registro_toma(db: Session, registro_id: int) -> bool:
    db_registro = get_registro_toma(db, registro_id)
    if not db_registro:
        return False
    db.delete(db_registro)
    db.commit()
    return True
