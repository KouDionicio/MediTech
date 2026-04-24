from sqlalchemy.orm import Session
from app.models.medicamento import Medicamento
from app.schemas.medicamento import MedicamentoCreate, MedicamentoUpdate


def get_medicamento(db: Session, medicamento_id: int) -> Medicamento | None:
    return db.query(Medicamento).filter(Medicamento.id == medicamento_id).first()


def get_medicamentos_by_usuario(db: Session, usuario_id: int, skip: int = 0, limit: int = 100):
    return db.query(Medicamento).filter(Medicamento.usuario_id == usuario_id).offset(skip).limit(limit).all()


def get_medicamentos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Medicamento).offset(skip).limit(limit).all()


def create_medicamento(db: Session, medicamento: MedicamentoCreate) -> Medicamento:
    db_medicamento = Medicamento(
        usuario_id=medicamento.usuario_id,
        nombre=medicamento.nombre,
        dosis=medicamento.dosis,
        presentacion=medicamento.presentacion,
        cantidad_total=medicamento.cantidad_total,
        stock_minimo=medicamento.stock_minimo,
        estatus=medicamento.estatus,
    )
    db.add(db_medicamento)
    db.commit()
    db.refresh(db_medicamento)
    return db_medicamento


def update_medicamento(db: Session, medicamento_id: int, update: MedicamentoUpdate) -> Medicamento | None:
    db_medicamento = get_medicamento(db, medicamento_id)
    if not db_medicamento:
        return None
    for field, value in update.model_dump(exclude_unset=True).items():
        setattr(db_medicamento, field, value)
    db.commit()
    db.refresh(db_medicamento)
    return db_medicamento


def delete_medicamento(db: Session, medicamento_id: int) -> bool:
    db_medicamento = get_medicamento(db, medicamento_id)
    if not db_medicamento:
        return False
    db.delete(db_medicamento)
    db.commit()
    return True