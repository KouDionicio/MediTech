from fastapi import FastAPI
from core.config import settings

from routers.usuario import router as usuario_router
from routers.dispositivo import router as dispositivo_router
from routers.medicamento import router as medicamento_router
from routers.horario import router as horario_router
from routers.registro_toma import router as registro_toma_router
from routers.alerta import router as alerta_router
from routers.auth import router as auth_router

app = FastAPI(
    title="MediTech MedAlert + API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


# Routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(usuario_router, prefix="/api/usuarios", tags=["Usuarios"])
app.include_router(dispositivo_router, prefix="/api/dispositivos", tags=["Dispositivos"])
app.include_router(medicamento_router, prefix="/api/medicamentos", tags=["Medicamentos"])
app.include_router(horario_router, prefix="/api/horarios", tags=["Horarios"])
app.include_router(registro_toma_router, prefix="/api/registros-toma", tags=["Registros"])
app.include_router(alerta_router, prefix="/api/alertas", tags=["Alertas"])


@app.get("/")
def root():
    return {
        "message": "MediTech API running",
        "environment": settings.environment
    }