from sqlalchemy.orm import Session
from models.alerta import Alerta
from schemas.alerta import AlertaCreate, AlertaUpdate


def get_alerta(db: Session, alerta_id: int) -> Alerta | None:
    return db.query(Alerta).filter(Alerta.id == alerta_id).first()


def get_alertas_by_usuario(db: Session, usuario_id: int, skip: int = 0, limit: int = 100):
    return db.query(Alerta).filter(Alerta.usuario_id == usuario_id).offset(skip).limit(limit).all()


def get_alertas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Alerta).offset(skip).limit(limit).all()


def create_alerta(db: Session, alerta: AlertaCreate) -> Alerta:
    db_alerta = Alerta(
        usuario_id=alerta.usuario_id,
        tipo_alerta=alerta.tipo_alerta,
        mensaje=alerta.mensaje,
        leida=alerta.leida,
    )
    db.add(db_alerta)
    db.commit()
    db.refresh(db_alerta)
    return db_alerta


def update_alerta(db: Session, alerta_id: int, update: AlertaUpdate) -> Alerta | None:
    db_alerta = get_alerta(db, alerta_id)
    if not db_alerta:
        return None
    for field, value in update.model_dump(exclude_unset=True).items():
        setattr(db_alerta, field, value)
    db.commit()
    db.refresh(db_alerta)
    return db_alerta


def delete_alerta(db: Session, alerta_id: int) -> bool:
    db_alerta = get_alerta(db, alerta_id)
    if not db_alerta:
        return False
    db.delete(db_alerta)
    db.commit()
    return True
