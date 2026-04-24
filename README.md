<div align="center">

<h1>💊 MedAlert +</h1>
<h3>Pastillero Inteligente con IoT — Sistema de Adherencia Terapéutica</h3>

<p><em>Dispositivo inteligente integrado a una botella con sensores, recordatorios y conectividad a una app multiplataforma para monitoreo en tiempo real</em></p>

<br/>

![Python](https://img.shields.io/badge/Python-3.11-FFD43B?style=for-the-badge&logo=python&logoColor=black)
![FastAPI](https://img.shields.io/badge/FastAPI-0.128.0-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-Auth-black?style=for-the-badge&logo=JSON%20web%20tokens)
![IoT](https://img.shields.io/badge/IoT-Sensores-FF6C37?style=for-the-badge&logo=arduino&logoColor=white)

![REST](https://img.shields.io/badge/API-REST-6c757d?style=flat-square)
![CORS](https://img.shields.io/badge/CORS-Enabled-28a745?style=flat-square)
![Swagger](https://img.shields.io/badge/Swagger-Docs-85EA2D?style=flat-square&logo=swagger&logoColor=black)
![WebSockets](https://img.shields.io/badge/WebSockets-Tiempo%20Real-4A90E2?style=flat-square)
![Status](https://img.shields.io/badge/Estado-En%20Desarrollo-orange?style=flat-square)

</div>

---

## 📋 Descripción General

**MedAlert +** es un pastillero inteligente integrado a una botella con tecnología IoT que ayuda a gestionar la medicación con sensores, recordatorios y conectividad a una app móvil y web, permitiendo el monitoreo en tiempo real. El sistema permite a usuarios y cuidadores monitorear la toma de medicamentos y consultar el historial de consumo en la aplicación.

> El proyecto soluciona la problemática de olvido de medicamentos en adultos mayores y pacientes crónicos, mejorando la adherencia al tratamiento mediante alertas visuales, sonoras y monitoreo remoto.

---

## 🎯 Problemática

Muchas personas olvidan tomar sus medicamentos, lo que afecta su salud y puede derivar en complicaciones graves. Los tratamientos crónicos requieren una adherencia estricta que, sin recordatorios adecuados, resulta difícil de mantener especialmente en adultos mayores o personas con múltiples medicamentos.

**MedAlert +** soluciona esto con:
- Recordatorios inteligentes (visuales y sonoros)
- Monitoreo remoto para cuidadores
- Control preciso de horarios y dosis

---

## 🎯 Objetivo General

Desarrollar un prototipo de pastillero inteligente integrado a una botella y vinculado a una app multiplataforma, mejorando el acceso y cumplimiento del tratamiento médico.

---

## 📌 Objetivos Específicos

1. Definir hardware y software del proyecto.
2. Diseñar y maquetar el prototipo.
3. Desarrollar software y base de datos.
4. Realizar pruebas y documentarlas.
5. Implementar mejoras según sea necesario.

---

## 👥 Público Objetivo

| Segmento | Descripción |
|----------|-------------|
| **Adultos Mayores** | Personas que requieren apoyo para administrar sus medicamentos sin depender de aplicaciones complejas |
| **Pacientes Crónicos** | Personas con diabetes, hipertensión, etc. que necesitan control preciso de su medicación |
| **Cuidadores y Familiares** | Personas que desean monitorear a distancia el cumplimiento del tratamiento |
| **Público General** | Personas que desean mejorar la adherencia a sus tratamientos médicos |

---

## 🏗️ Arquitectura de Seguridad

Todo el ecosistema está protegido utilizando el estándar de seguridad **JSON Web Tokens (JWT)**:

1. La llave de acceso central es el endpoint público de `Login`.
2. Una vez autorizado, las llamadas viajan con un **Token Bearer (HTTPBearer)** validado en cada petición.
3. Las contraseñas nunca se almacenan en texto plano — se hashean con `Passlib` (`sha256_crypt`).
4. Las políticas **CORS** están configuradas para garantizar compatibilidad con el frontend y apps móviles.

---

## 📁 Estructura del Proyecto
MedAlert+/
│
├── api/
│ ├── init.py
│ ├── app.py # Punto de entrada de la aplicación
│ ├── jwt_config.py # Configuración de JWT
│ └── portadortoken.py # Middleware de autenticación Bearer
│
├── config/
│ └── db.py # Configuración de conexión a MySQL
│
├── crud/
│ ├── alerta.py # CRUD de alertas
│ ├── dispositivo.py # CRUD de dispositivos IoT
│ ├── horario.py # CRUD de horarios
│ ├── medicamento.py # CRUD de medicamentos
│ ├── registro_toma.py # CRUD de registros de toma
│ └── usuario.py # CRUD de usuarios
│
├── dashboard/
│ └── ... # Panel de administración web
│
├── db/
│ └── ... # Modelos y conexión a BD
│
├── docs/
│ └── ... # Documentación del proyecto
│
├── hardware/
│ ├── firmware/ # Código del dispositivo IoT
│ └── schematics/ # Diagramas electrónicos
│
├── images/
│ └── diagrama_erd.jpeg # Diagrama ERD del sistema
│
├── mobile/
│ └── ... # App móvil (React Native/Flutter)
│
├── models/
│ └── models_ma/
│ ├── init.py
│ ├── alerta.py # Modelo de alertas
│ ├── dispositivo.py # Modelo de dispositivos IoT
│ ├── horario.py # Modelo de horarios
│ ├── medicamento.py # Modelo de medicamentos
│ ├── registro_toma.py # Modelo de registros de toma
│ └── usuario.py # Modelo de usuarios
│
├── routers/
│ ├── init.py
│ ├── alertas.py # Endpoints de alertas
│ ├── auth.py # Endpoints de autenticación
│ ├── dispositivos.py # Endpoints de dispositivos
│ ├── horarios.py # Endpoints de horarios
│ ├── medicamentos.py # Endpoints de medicamentos
│ ├── registros.py # Endpoints de registros de toma
│ └── usuarios.py # Endpoints de usuarios
│
├── schemas/
│ └── schemas_ma/
│ ├── init.py
│ ├── alerta.py # Schema de alertas
│ ├── dispositivo.py # Schema de dispositivos
│ ├── horario.py # Schema de horarios
│ ├── medicamento.py # Schema de medicamentos
│ ├── registro_toma.py # Schema de registros de toma
│ └── usuario.py # Schema de usuarios
│
├── tests/
│ └── ... # Pruebas unitarias e integración
│
├── .env # Variables de entorno
├── .gitignore
├── BRs.md # Business Requirements
├── FRs.md # Functional Requirements
├── NFRs.md # Non-Functional Requirements
├── requirements.txt # Dependencias del backend
└── README.md # Documentación principal

text

---

## 🔧 Modelos de Dominio

El sistema MedAlert + cubre el flujo completo de adherencia terapéutica:

1. **Usuario** — Pacientes y cuidadores con perfiles y roles diferenciados.
2. **Dispositivo** — Pastillero inteligente con sensores y conectividad.
3. **Medicamento** — Catálogo de medicamentos con horarios y dosis.
4. **Horario** — Programación de tomas con recordatorios configurables.
5. **RegistroToma** — Historial de tomas realizadas y omitidas.
6. **Alerta** — Notificaciones generadas por omisión o próxima toma.

---

## 📊 Modelos del Sistema

### 🔹 `Usuario`
Representa a los usuarios del sistema (pacientes y cuidadores).

| Campo | Tipo | Restricción | Descripción |
|---|---|---|---|
| `Id` | `Integer` | PK, Autoincremental | Identificador único |
| `Nombre` | `String(100)` | No nulo | Nombre completo |
| `Email` | `String(100)` | No nulo, Único | Correo electrónico |
| `Telefono` | `String(20)` | Opcional | Número de contacto |
| `Rol` | `Enum` | No nulo | `PACIENTE` · `CUIDADOR` · `ADMIN` |
| `Password` | `String(255)` | No nulo | Hash de contraseña |
| `Fecha_Registro` | `DateTime` | Auto `now()` | Fecha de registro |

**Relaciones:** `Usuario` → `Dispositivo`, `RegistroToma`, `Alerta`

---

### 🔹 `Dispositivo`
Representa el pastillero inteligente MedAlert +.

| Campo | Tipo | Restricción | Descripción |
|---|---|---|---|
| `Id` | `Integer` | PK, Autoincremental | Identificador único |
| `Usuario_Id` | `Integer` | FK → `usuario.Id` | Dueño del dispositivo |
| `Mac_Address` | `String(17)` | No nulo, Único | Dirección MAC del dispositivo |
| `Nombre_Dispositivo` | `String(100)` | Opcional | Nombre asignado por el usuario |
| `Estado` | `Enum` | No nulo | `ACTIVO` · `INACTIVO` · `MANTENIMIENTO` |
| `Nivel_Bateria` | `Integer` | Default: 100 | Porcentaje de batería |
| `Ultima_Conexion` | `DateTime` | Auto `now()` | Última vez que envió datos |
| `Fecha_Registro` | `DateTime` | Auto `now()` | Fecha de registro |

**Relaciones:** `Dispositivo` → `Usuario`, `Horario`, `RegistroToma`

---

### 🔹 `Medicamento`
Catálogo de medicamentos del paciente.

| Campo | Tipo | Restricción | Descripción |
|---|---|---|---|
| `Id` | `Integer` | PK, Autoincremental | Identificador único |
| `Usuario_Id` | `Integer` | FK → `usuario.Id` | Paciente asociado |
| `Nombre` | `String(150)` | No nulo | Nombre del medicamento |
| `Dosis` | `String(50)` | No nulo | Cantidad por toma (mg, ml) |
| `Presentacion` | `String(100)` | No nulo | Tabletas, jarabe, cápsulas |
| `Cantidad_Total` | `Integer` | No nulo | Stock disponible |
| `Stock_Minimo` | `Integer` | Default: 5 | Alerta de bajo stock |
| `Estatus` | `Boolean` | Default: `True` | Activo/Inactivo |

**Relaciones:** `Medicamento` → `Usuario`, `Horario`, `RegistroToma`

---

### 🔹 `Horario`
Programación de tomas para cada medicamento.

| Campo | Tipo | Restricción | Descripción |
|---|---|---|---|
| `Id` | `Integer` | PK, Autoincremental | Identificador único |
| `Medicamento_Id` | `Integer` | FK → `medicamento.Id` | Medicamento asociado |
| `Hora_Toma` | `Time` | No nulo | Hora programada |
| `Dias_Semana` | `String(50)` | No nulo | L,MX,J,V,S,D (JSON array) |
| `Duracion_Tratamiento` | `Integer` | Opcional | Días de duración |
| `Fecha_Inicio` | `Date` | No nulo | Fecha de inicio |
| `Fecha_Fin` | `Date` | Opcional | Fecha de término |

**Relaciones:** `Horario` → `Medicamento`

---

### 🔹 `RegistroToma`
Historial de tomas realizadas u omitidas.

| Campo | Tipo | Restricción | Descripción |
|---|---|---|---|
| `Id` | `Integer` | PK, Autoincremental | Identificador único |
| `Horario_Id` | `Integer` | FK → `horario.Id` | Horario asociado |
| `Fecha_Hora_Programada` | `DateTime` | No nulo | Fecha y hora programada |
| `Fecha_Hora_Toma` | `DateTime` | Opcional | Fecha y hora real de toma |
| `Estado` | `Enum` | No nulo | `TOMADO` · `OMITIDO` · `PENDIENTE` |
| `Confirmado_Por` | `Enum` | Opcional | `USUARIO` · `SENSOR` · `CUIDADOR` |

**Relaciones:** `RegistroToma` → `Horario`

---

### 🔹 `Alerta`
Notificaciones generadas por el sistema.

| Campo | Tipo | Restricción | Descripción |
|---|---|---|---|
| `Id` | `Integer` | PK, Autoincremental | Identificador único |
| `Usuario_Id` | `Integer` | FK → `usuario.Id` | Usuario destino |
| `Tipo_Alerta` | `Enum` | No nulo | `TOMA_PENDIENTE` · `TOMA_OMITIDA` · `STOCK_BAJO` · `DISPOSITIVO_DESCONECTADO` |
| `Mensaje` | `Text` | No nulo | Descripción de la alerta |
| `Leida` | `Boolean` | Default: `False` | Si fue vista por el usuario |
| `Fecha_Alerta` | `DateTime` | Auto `now()` | Fecha de generación |

**Relaciones:** `Alerta` → `Usuario`

---

## 📊 Diagrama de Relaciones (ERD)
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│ Usuario │────<│ Dispositivo │ │ Horario │
└──────┬──────┘ └─────────────┘ └──────▲──────┘
│ │
│ ┌─────────────┐ ┌─────────────┐│
└────<│ Medicamento │────<│ RegistroToma││
└──────┬──────┘ └─────────────┘│
│ │
└───────────────────────────┘

┌─────────────┐
│ Alerta │
└──────▲──────┘
│
└────── Usuario_Id (FK)

text

**Relaciones del modelo:**
- Un **Usuario** puede tener múltiples **Dispositivos**, **Medicamentos** y **Alertas**
- Un **Dispositivo** pertenece a un solo **Usuario**
- Un **Medicamento** pertenece a un solo **Usuario**
- Un **Medicamento** puede tener múltiples **Horarios**
- Un **Horario** puede tener múltiples **RegistrosToma**
- Una **Alerta** pertenece a un solo **Usuario**

---

## ⚙️ Tecnologías

| Tecnología | Versión | Uso |
|---|---|---|
| Python | 3.11 | Lenguaje principal del backend |
| FastAPI | 0.128.0 | Framework web y generación de API REST |
| SQLAlchemy | 2.0.48 | ORM para manejo de base de datos |
| Pydantic | 2.12.5 | Validación de datos y schemas |
| MySQL | 8.0 | Motor de base de datos relacional |
| PyMySQL | 1.1.2 | Driver de conexión MySQL |
| PyJWT | 2.12.1 | Generación y validación de JWT |
| WebSockets | 16.00 | Comunicación en tiempo real con IoT |
| PyQt6 | 6.10.0 | Interfaz para dashboard de escritorio |
| Uvicorn | 0.40.0 | Servidor ASGI |
| Cryptography | 46.0.3 | Encriptación de datos sensibles |

---


## 🚀 Guía de Inicialización Rápida

Abre la rama principal o clona el repositorio e hidrata el entorno virtual así:

**1. Clona el repositorio:**
```bash
git clone https://github.com/tu-usuario/MedAlertPlus.git
cd MedAlertPlus
```

**2. Crea y activa el entorno virtual:**
```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
```
**4. Instala las dependencias:**

```bash
pip install -r requirements.txt
```

**5. Ejecuta las migraciones / creación de tablas:**

```bash
python -c "from config.db import Base, engine; Base.metadata.create_all(engine)"
```

**6. Levanta el servidor de desarrollo:**

```bash
python -m uvicorn api.app:app --reload
```


##  Integrantes

| # | Nombre | GitHub |
|---|--------|--------|
| 1 | Yazmin Gutierrez Hernandez | [@YazUtxj](https://github.com/YazUtxj) | 
| 2 | Obed Guzman Flores | [@ObedGuzmanGuz](https://github.com/ObedGuzmanGuz) | 
| 3 | Michelle Castro Otero | [@Ktmich2095](https://github.com/Ktmich2095) | 
| 4 | Citlalli Pérez Dionicio | [@KouDionicio](https://github.com/KouDionicio) | 

---