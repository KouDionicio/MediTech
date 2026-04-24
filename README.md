<div align="center">

# MedAlert+
### Pastillero Inteligente con IoT — Sistema de Adherencia Terapéutica

*Dispositivo inteligente con sensores integrados, recordatorios inteligentes y conectividad a una app multiplataforma para monitoreo en tiempo real del tratamiento médico.*

<br/>

[![Python](https://img.shields.io/badge/Python-3.11-FFD43B?style=for-the-badge&logo=python&logoColor=black)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.128.0-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?style=for-the-badge&logo=python&logoColor=white)](https://www.sqlalchemy.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![JWT](https://img.shields.io/badge/JWT-Auth-black?style=for-the-badge&logo=JSON%20web%20tokens)](https://jwt.io/)
[![IoT](https://img.shields.io/badge/IoT-Sensores-FF6C37?style=for-the-badge&logo=arduino&logoColor=white)](https://www.arduino.cc/)

![REST](https://img.shields.io/badge/API-REST-6c757d?style=flat-square)
![CORS](https://img.shields.io/badge/CORS-Enabled-28a745?style=flat-square)
![Swagger](https://img.shields.io/badge/Docs-Swagger-85EA2D?style=flat-square&logo=swagger&logoColor=black)
![WebSockets](https://img.shields.io/badge/WebSockets-Tiempo%20Real-4A90E2?style=flat-square)
![Status](https://img.shields.io/badge/Estado-En%20Desarrollo-orange?style=flat-square)

</div>

---

## Descripción General

**MedAlert+** es un sistema de adherencia terapéutica que combina hardware IoT (pastillero inteligente integrado a una botella con sensores) con software backend y una app multiplataforma. Permite a pacientes y cuidadores monitorear en tiempo real la toma de medicamentos, recibir alertas y consultar el historial de consumo desde cualquier dispositivo.

> **Problemática:** El olvido de medicamentos afecta especialmente a adultos mayores y pacientes crónicos, derivando en complicaciones graves y hospitalizaciones evitables. MedAlert+ responde con recordatorios visuales y sonoros, confirmación automática por sensor, y monitoreo remoto para cuidadores — sin requerir conocimientos técnicos del usuario final.

---

## Tabla de Contenidos

- [MedAlert+](#medalert)
    - [Pastillero Inteligente con IoT — Sistema de Adherencia Terapéutica](#pastillero-inteligente-con-iot--sistema-de-adherencia-terapéutica)
  - [Descripción General](#descripción-general)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Características Principales](#características-principales)
  - [Arquitectura del Sistema](#arquitectura-del-sistema)
  - [Tecnologías](#tecnologías)
  - [Estructura del Proyecto](#estructura-del-proyecto)
  - [Modelos de Dominio](#modelos-de-dominio)
    - [`Usuario`](#usuario)
    - [`Dispositivo`](#dispositivo)
    - [`Medicamento`](#medicamento)
    - [`Horario`](#horario)
    - [`RegistroToma`](#registrotoma)
    - [`Alerta`](#alerta)
    - [Diagrama ERD](#diagrama-erd)
  - [Seguridad](#seguridad)
  - [Guía de Instalación](#guía-de-instalación)
    - [Prerrequisitos](#prerrequisitos)
    - [Pasos](#pasos)
  - [Endpoints de la API](#endpoints-de-la-api)
  - [Público Objetivo](#público-objetivo)
  - [Objetivos del Proyecto](#objetivos-del-proyecto)
  - [Equipo](#equipo)

---

## Características Principales

| Característica | Descripción |
|---|---|
| **Recordatorios inteligentes** | Alertas visuales y sonoras configurables por horario |
| **Conectividad IoT** | El dispositivo reporta el estado en tiempo real vía WebSockets |
| **Historial de tomas** | Registro completo de tomas realizadas, omitidas y pendientes |
| **Modo cuidador** | Monitoreo remoto con notificaciones de omisión |
| **Estado del dispositivo** | Control de batería, última conexión y estado operativo |
| **Control de stock** | Alertas automáticas cuando el medicamento está por agotarse |
| **Seguridad JWT** | Autenticación robusta con tokens Bearer en cada petición |

---

## Arquitectura del Sistema

```
┌──────────────┐        ┌──────────────────────┐        ┌───────────────┐
│  Dispositivo │◄──────►│   Backend FastAPI     │◄──────►│  App Móvil /  │
│  IoT (HW)   │        │   + MySQL + WebSocket │        │  Dashboard    │
└──────────────┘        └──────────────────────┘        └───────────────┘
     Sensores                   JWT Auth                   React Native
     Firmware                   REST API                   PyQt6 Desktop
     Alertas LED                CRUD Services              Notificaciones
```

El flujo general es:
1. El **dispositivo IoT** detecta la apertura/cierre del pastillero mediante sensores.
2. Reporta el evento al **backend FastAPI** vía WebSocket o HTTP.
3. El backend actualiza el `RegistroToma`, genera `Alertas` si aplica y persiste en **MySQL**.
4. La **app móvil o dashboard** consulta el estado y muestra el historial al usuario o cuidador.

---

## Tecnologías

| Tecnología | Versión | Rol |
|---|---|---|
| **Python** | 3.11 | Lenguaje principal del backend |
| **FastAPI** | 0.128.0 | Framework web y generación de API REST |
| **SQLAlchemy** | 2.0.48 | ORM para manejo de base de datos |
| **Pydantic** | 2.12.5 | Validación de datos y schemas |
| **MySQL** | 8.0 | Motor de base de datos relacional |
| **PyMySQL** | 1.1.2 | Driver de conexión MySQL |
| **PyJWT** | 2.12.1 | Generación y validación de JWT |
| **WebSockets** | 16.0 | Comunicación en tiempo real con el dispositivo IoT |
| **PyQt6** | 6.10.0 | Dashboard de escritorio |
| **Uvicorn** | 0.40.0 | Servidor ASGI de producción |
| **Cryptography** | 46.0.3 | Encriptación de datos sensibles |

---

## Estructura del Proyecto

```
MedAlert+/
│
├── api/
│   ├── py              # Punto de entrada, configuración FastAPI y CORS
│   ├── jwt_config.py       # Configuración y helpers de JWT
│   └── portadortoken.py    # Middleware de autenticación Bearer
│
├── config/
│   └── db.py               # Conexión y sesión de MySQL con SQLAlchemy
│
├── models/models_ma/       # Modelos ORM (tablas de la base de datos)
│   ├── usuario.py
│   ├── dispositivo.py
│   ├── medicamento.py
│   ├── horario.py
│   ├── registro_toma.py
│   └── alerta.py
│
├── schemas/schemas_ma/     # Schemas Pydantic para validación y serialización
│   ├── usuario.py
│   ├── dispositivo.py
│   ├── medicamento.py
│   ├── horario.py
│   ├── registro_toma.py
│   └── alerta.py
│
├── crud/                   # Lógica de acceso a datos (Create, Read, Update, Delete)
│   ├── usuario.py
│   ├── dispositivo.py
│   ├── medicamento.py
│   ├── horario.py
│   ├── registro_toma.py
│   └── alerta.py
│
├── routers/                # Endpoints REST agrupados por recurso
│   ├── auth.py             # Login y refresh de tokens
│   ├── usuarios.py
│   ├── dispositivos.py
│   ├── medicamentos.py
│   ├── horarios.py
│   ├── registros.py
│   └── alertas.py
│
├── hardware/
│   ├── firmware/           # Código del microcontrolador IoT
│   └── schematics/         # Diagramas electrónicos del circuito
│
├── dashboard/              # Panel de administración web (PyQt6)
├── mobile/                 # App móvil (React Native / Flutter)
├── tests/                  # Pruebas unitarias e integración
├── docs/                   # Documentación técnica adicional
├── images/
│   └── diagrama_erd.jpeg   # Diagrama ERD del sistema
│
├── .env                    # Variables de entorno (no incluir en VCS)
├── requirements.txt        # Dependencias del backend
├── BRs.md                  # Business Requirements
├── FRs.md                  # Functional Requirements
├── NFRs.md                 # Non-Functional Requirements
└── README.md
```

---

## Modelos de Dominio

El sistema cubre el flujo completo de adherencia terapéutica a través de seis entidades principales:

### `Usuario`
Pacientes y cuidadores con roles diferenciados.

| Campo | Tipo | Descripción |
|---|---|---|
| `Id` | `Integer` PK | Identificador único |
| `Nombre` | `String(100)` | Nombre completo |
| `Email` | `String(100)` único | Correo electrónico |
| `Telefono` | `String(20)` | Número de contacto (opcional) |
| `Rol` | `Enum` | `PACIENTE` · `CUIDADOR` · `ADMIN` |
| `Password` | `String(255)` | Hash de contraseña (sha256_crypt) |
| `Fecha_Registro` | `DateTime` | Automático al crear |

---

### `Dispositivo`
Representa el pastillero inteligente MedAlert+.

| Campo | Tipo | Descripción |
|---|---|---|
| `Id` | `Integer` PK | Identificador único |
| `Usuario_Id` | FK → `usuario` | Dueño del dispositivo |
| `Mac_Address` | `String(17)` único | Dirección MAC del hardware |
| `Nombre_Dispositivo` | `String(100)` | Alias asignado por el usuario |
| `Estado` | `Enum` | `ACTIVO` · `INACTIVO` · `MANTENIMIENTO` |
| `Nivel_Bateria` | `Integer` | Porcentaje (default: 100) |
| `Ultima_Conexion` | `DateTime` | Último reporte del dispositivo |

---

### `Medicamento`
Catálogo de medicamentos del paciente.

| Campo | Tipo | Descripción |
|---|---|---|
| `Id` | `Integer` PK | Identificador único |
| `Usuario_Id` | FK → `usuario` | Paciente propietario |
| `Nombre` | `String(150)` | Nombre del medicamento |
| `Dosis` | `String(50)` | Cantidad por toma (mg, ml, etc.) |
| `Presentacion` | `String(100)` | Tabletas, jarabe, cápsulas... |
| `Cantidad_Total` | `Integer` | Stock disponible |
| `Stock_Minimo` | `Integer` | Umbral de alerta (default: 5) |
| `Estatus` | `Boolean` | Activo/Inactivo (default: True) |

---

### `Horario`
Programación de tomas para cada medicamento.

| Campo | Tipo | Descripción |
|---|---|---|
| `Id` | `Integer` PK | Identificador único |
| `Medicamento_Id` | FK → `medicamento` | Medicamento asociado |
| `Hora_Toma` | `Time` | Hora programada |
| `Dias_Semana` | `String(50)` | Días en formato JSON: `["L","MX","V"]` |
| `Duracion_Tratamiento` | `Integer` | Días de duración (opcional) |
| `Fecha_Inicio` | `Date` | Inicio del tratamiento |
| `Fecha_Fin` | `Date` | Fin del tratamiento (opcional) |

---

### `RegistroToma`
Historial de tomas realizadas u omitidas.

| Campo | Tipo | Descripción |
|---|---|---|
| `Id` | `Integer` PK | Identificador único |
| `Horario_Id` | FK → `horario` | Horario asociado |
| `Fecha_Hora_Programada` | `DateTime` | Cuándo debía tomarse |
| `Fecha_Hora_Toma` | `DateTime` | Cuándo se tomó realmente (opcional) |
| `Estado` | `Enum` | `TOMADO` · `OMITIDO` · `PENDIENTE` |
| `Confirmado_Por` | `Enum` | `USUARIO` · `SENSOR` · `CUIDADOR` |

---

### `Alerta`
Notificaciones generadas automáticamente por el sistema.

| Campo | Tipo | Descripción |
|---|---|---|
| `Id` | `Integer` PK | Identificador único |
| `Usuario_Id` | FK → `usuario` | Usuario destinatario |
| `Tipo_Alerta` | `Enum` | `TOMA_PENDIENTE` · `TOMA_OMITIDA` · `STOCK_BAJO` · `DISPOSITIVO_DESCONECTADO` |
| `Mensaje` | `Text` | Descripción de la alerta |
| `Leida` | `Boolean` | Si fue vista (default: False) |
| `Fecha_Alerta` | `DateTime` | Automático al generar |

---

### Diagrama ERD

```
┌──────────────┐     1:N     ┌─────────────────┐
│   Usuario    │────────────►│   Dispositivo   │
│              │             └─────────────────┘
│              │     1:N     ┌─────────────────┐     1:N     ┌─────────────────┐
│              │────────────►│   Medicamento   │────────────►│    Horario      │
│              │             └─────────────────┘             └────────┬────────┘
│              │     1:N     ┌─────────────────┐                      │ 1:N
│              │────────────►│     Alerta      │             ┌────────▼────────┐
└──────────────┘             └─────────────────┘             │  RegistroToma  │
                                                             └─────────────────┘
```

**Reglas de negocio:**
- Un **Usuario** puede tener múltiples Dispositivos, Medicamentos y Alertas.
- Un **Medicamento** pertenece a un único Usuario y puede tener múltiples Horarios.
- Un **Horario** genera múltiples RegistrosToma (uno por cada toma programada).
- Una **Alerta** siempre está asociada a un Usuario destino.

---

## Seguridad

Todo el ecosistema está protegido con el estándar **JSON Web Tokens (JWT)**:

1. El endpoint público `/auth/login` devuelve un **Access Token** al autenticarse correctamente.
2. Todas las peticiones protegidas deben incluir el header `Authorization: Bearer <token>`.
3. El middleware `portadortoken.py` valida el token en cada request antes de llegar al router.
4. Las contraseñas se hashean con `Passlib` usando `sha256_crypt` — nunca se almacenan en texto plano.
5. Las políticas **CORS** están configuradas para permitir acceso desde el frontend y las apps móviles.

---

## Guía de Instalación

### Prerrequisitos

- Python 3.11+
- MySQL 8.0 corriendo localmente o en la nube
- Git

### Pasos

**1. Clonar el repositorio**
```bash
git clone https://github.com/KouDionicio/MediTech.git
cd MediTech
```

**2. Crear y activar el entorno virtual**
```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**3. Instalar dependencias**
```bash
pip install -r requirements.txt
```

**4. Configurar variables de entorno**

Crea un archivo `.env` en la raíz del proyecto:
```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=medalert_db
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
JWT_SECRET=tu_clave_secreta_muy_segura
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60
```

**5. Crear las tablas en la base de datos**
```bash
python -c "from config.db import Base, engine; meditech.metadata.create_all(engine)"
```

**6. Levantar el servidor**
```bash
python -m uvicorn main:app --reload
```

El servidor estará disponible en `http://localhost:8000`.
La documentación interactiva (Swagger) en `http://localhost:8000/docs`.

---

## Endpoints de la API

| Método | Ruta | Descripción | Auth |
|---|---|---|---|
| `POST` | `/auth/login` | Obtener token JWT | No |
| `GET` | `/usuarios/` | Listar usuarios | Si |
| `POST` | `/usuarios/` | Crear usuario | Si |
| `GET` | `/dispositivos/` | Listar dispositivos | Si |
| `POST` | `/dispositivos/` | Registrar dispositivo | Si |
| `GET` | `/medicamentos/` | Listar medicamentos | Si |
| `POST` | `/medicamentos/` | Agregar medicamento | Si |
| `GET` | `/horarios/` | Listar horarios | Si |
| `POST` | `/horarios/` | Crear horario | Si |
| `GET` | `/registros/` | Historial de tomas | Si |
| `POST` | `/registros/` | Registrar toma | Si |
| `GET` | `/alertas/` | Ver alertas del usuario | Si |
| `PATCH` | `/alertas/{id}/leer` | Marcar alerta como leída | Si |

---

## Público Objetivo

| Segmento | Necesidad |
|---|---|
| **Adultos Mayores** | Recordatorios simples sin interfaces complejas |
| **Pacientes Crónicos** | Control preciso de horarios y dosis (diabetes, hipertensión...) |
| **Cuidadores y Familiares** | Monitoreo remoto y alertas por omisión |
| **Público General** | Mejorar la adherencia a cualquier tratamiento médico |

---

## Objetivos del Proyecto

**General:** Desarrollar un prototipo de pastillero inteligente vinculado a una app multiplataforma que mejore el acceso y cumplimiento del tratamiento médico.

**Específicos:**
1. Definir el stack de hardware y software del sistema.
2. Diseñar y maquetar el prototipo físico y las interfaces digitales.
3. Desarrollar el backend, la base de datos y las integraciones IoT.
4. Realizar pruebas funcionales y documentar resultados.
5. Implementar mejoras iterativas según retroalimentación.

---

## Equipo

| # | Nombre | GitHub |
|---|--------|--------|
| 1 | Yazmin Gutierrez Hernandez | [@YazUtxj](https://github.com/YazUtxj) |
| 2 | Obed Guzman Flores | [@ObedGuzmanGuz](https://github.com/ObedGuzmanGuz) |
| 3 | Michelle Castro Otero | [@Ktmich2095](https://github.com/Ktmich2095) |
| 4 | Citlalli Pérez Dionicio | [@KouDionicio](https://github.com/KouDionicio) |

---

<div align="center">

Hecho para mejorar la salud y calidad de vida de las personas.

</div>