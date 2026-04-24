from sqlalchemy.orm import Session
from app.models.dispositivo import Dispositivo
from app.schemas.dispositivo import DispositivoCreate, DispositivoUpdate


def get_dispositivo(db: Session, dispositivo_id: int) -> Dispositivo | None:
    return db.query(Dispositivo).filter(Dispositivo.id == dispositivo_id).first()


def get_dispositivo_by_mac(db: Session, mac_address: str) -> Dispositivo | None:
    return db.query(Dispositivo).filter(Dispositivo.mac_address == mac_address).first()


def get_dispositivos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Dispositivo).offset(skip).limit(limit).all()


def create_dispositivo(db: Session, dispositivo: DispositivoCreate) -> Dispositivo:
    db_dispositivo = Dispositivo(
        usuario_id=dispositivo.usuario_id,
        mac_address=dispositivo.mac_address,
        nombre_dispositivo=dispositivo.nombre_dispositivo,
        estado=dispositivo.estado,
        nivel_bateria=dispositivo.nivel_bateria,
    )
    db.add(db_dispositivo)
    db.commit()
    db.refresh(db_dispositivo)
    return db_dispositivo


def update_dispositivo(db: Session, dispositivo_id: int, update: DispositivoUpdate) -> Dispositivo | None:
    db_dispositivo = get_dispositivo(db, dispositivo_id)
    if not db_dispositivo:
        return None
    for field, value in update.model_dump(exclude_unset=True).items():
        setattr(db_dispositivo, field, value)
    db.commit()
    db.refresh(db_dispositivo)
    return db_dispositivo


def delete_dispositivo(db: Session, dispositivo_id: int) -> bool:
    db_dispositivo = get_dispositivo(db, dispositivo_id)
    if not db_dispositivo:
        return False
    db.delete(db_dispositivo)
    db.commit()
    return True