from fastapi import FastAPI
from app.core.config import settings
from app.db.session import engine
from app.models import usuario as usuario_model, dispositivo as dispositivo_model, medicamento as medicamento_model
from app.models import horario as horario_model, registro_toma as registro_toma_model, alerta as alerta_model
from app.routers import usuario, dispositivo, medicamento, horario, registro_toma, alerta

# Crear todas las tablas definidas en los modelos
usuario_model.Usuario.metadata.create_all(bind=engine)
dispositivo_model.Dispositivo.metadata.create_all(bind=engine)
medicamento_model.Medicamento.metadata.create_all(bind=engine)
horario_model.Horario.metadata.create_all(bind=engine)
registro_toma_model.RegistroToma.metadata.create_all(bind=engine)
alerta_model.Alerta.metadata.create_all(bind=engine)

app = FastAPI(
    title="MediTech MedAlert + API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(usuario.router, prefix="/api/usuarios", tags=["Usuarios"])
app.include_router(dispositivo.router, prefix="/api/dispositivos", tags=["Dispositivos"])
app.include_router(medicamento.router, prefix="/api/medicamentos", tags=["Medicamentos"])
app.include_router(horario.router, prefix="/api/horarios", tags=["Horarios"])
app.include_router(registro_toma.router, prefix="/api/registros-toma", tags=["Registros de Toma"])
app.include_router(alerta.router, prefix="/api/alertas", tags=["Alertas"])


@app.get("/")
def root():
    return {"message": "MediTech MedAlert + API is running", "environment": settings.environment}
