# Sistema de Gestión de Eventos

## Información General

**Nombre del proyecto:** Sistema de Gestión de Eventos  
**Autor:** Angel Ducon Guaidia  
**Repositorio:** https://github.com/duconguaidia-spec/Sistema-Gestion-DeEventos/tree/feature_angel  
**Versión:** 1.0.0  

### Problema Desarrollado

Una empresa organizadora de eventos requiere administrar asistentes, eventos, sedes, organizadores, inscripciones, pagos, conferencias y patrocinadores. El sistema permite gestionar toda la información relacionada con la organización y ejecución de eventos mediante una API REST desarrollada con Django REST Framework y PostgreSQL, aplicando buenas prácticas de desarrollo empresarial.

---

## Tecnologías Utilizadas

| Tecnología | Descripción |
|---|---|
| Python 3.14 | Lenguaje de programación principal |
| Django 6.0.6 | Framework web backend |
| Django REST Framework | Construcción de la API REST |
| PostgreSQL | Motor de base de datos relacional |
| Swagger (drf-yasg) | Documentación interactiva de la API |
| djangorestframework-simplejwt | Autenticación mediante JSON Web Tokens |
| django-filter | Filtros avanzados en los endpoints |
| django-cors-headers | Manejo de CORS |
| openpyxl | Exportación de datos |
| python-decouple | Gestión de variables de entorno |

---

## Instalación

### Requisitos previos

- Python 3.10 o superior
- PostgreSQL instalado y en ejecución
- Git instalado

### 1. Clonación del repositorio

```bash
git clone https://github.com/duconguaidia-spec/Sistema-Gestion-DeEventos.git
cd Sistema-Gestion-DeEventos
git checkout feature_angel
```

### 2. Entorno virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en Linux o Mac
source venv/bin/activate
```

### 3. Instalación de dependencias

```bash
pip install -r requirements.txt
```

Contenido del archivo `requirements.txt`:
django
djangorestframework
djangorestframework-simplejwt
drf-yasg
psycopg2
django-filter
django-cors-headers
python-decouple
openpyxl

### 4. Variables de entorno

Copie el archivo de ejemplo y configure sus variables:

```bash
cp .env.example .env
```

Edite el archivo `.env` con sus credenciales:

API_PORT=el puerto en la que se va a correr el api
DEBUG=True
DB_NAME=el nombre de la base
DB_USER=nombre de usuario de la base
DB_PASSWORD=contraseña de la base
DB_HOST=direccion del servidor
DB_PORT=El puerto
DB_SCHEMA=Nonbre de SCHEMA

### 5. Configuración de base de datos

Asegúrese de que el schema de PostgreSQL exista antes de ejecutar las migraciones:

```sql
CREATE SCHEMA IF NOT EXISTS nombre_schema;
```

### 6. Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Creación de superusuario

```bash
python manage.py createsuperuser
```

---

## Ejecución

```bash
python manage.py runserver
```

El servidor estará disponible en:
http://127.0.0.1:8000

Documentación interactiva Swagger:
http://127.0.0.1:8000/swagger/

Panel de administración Django:
http://127.0.0.1:8000/admin/
---

## Autenticación

La API utiliza autenticación mediante JSON Web Token (JWT).

**Obtener token de acceso**

POST /api/token/

Cuerpo de la petición:

```json
{
    "username": "usuario",
    "password": "contrasena"
}
```

Respuesta exitosa:

```json
{
    "success": true,
    "message": "Token JWT generado correctamente.",
    "data": {
        "refresh": "token_refresh",
        "access": "token_access"
    },
    "errors": null
}
```

El token `access` debe enviarse en el encabezado de cada petición protegida:

Authorization: Bearer <token_access>

**Renovar token**
POST /api/token/refresh/

### Roles y Permisos

| Accion | Permiso requerido |
|---|---|
| GET (consultar) | Sin autenticacion |
| POST / PUT / PATCH | Rol Editor o Administrador |
| DELETE | Rol Administrador |

---

## Endpoints

Base URL: `http://127.0.0.1:8000/api/v1/`

### Autenticacion

| Metodo | Ruta | Descripcion |
|---|---|---|
| POST | `/api/token/` | Obtener token JWT |
| POST | `/api/token/refresh/` | Renovar token JWT |

### Sedes

| Metodo | Ruta | Descripcion |
|---|---|---|
| GET | `/api/v1/sedes/` | Listar sedes activas |
| POST | `/api/v1/sedes/` | Crear sede |
| GET | `/api/v1/sedes/{id}/` | Consultar sede |
| PUT | `/api/v1/sedes/{id}/` | Actualizar sede |
| PATCH | `/api/v1/sedes/{id}/` | Actualizar parcialmente |
| DELETE | `/api/v1/sedes/{id}/` | Eliminacion logica |
| GET | `/api/v1/sedes/exportar-csv/` | Exportar registros a CSV |

### Organizadores

| Metodo | Ruta | Descripcion |
|---|---|---|
| GET | `/api/v1/organizadores/` | Listar organizadores activos |
| POST | `/api/v1/organizadores/` | Crear organizador |
| GET | `/api/v1/organizadores/{id}/` | Consultar organizador |
| PUT | `/api/v1/organizadores/{id}/` | Actualizar organizador |
| PATCH | `/api/v1/organizadores/{id}/` | Actualizar parcialmente |
| DELETE | `/api/v1/organizadores/{id}/` | Eliminacion logica |
| GET | `/api/v1/organizadores/exportar-csv/` | Exportar registros a CSV |

### Eventos

| Metodo | Ruta | Descripcion |
|---|---|---|
| GET | `/api/v1/eventos/` | Listar eventos activos |
| POST | `/api/v1/eventos/` | Crear evento |
| GET | `/api/v1/eventos/{id}/` | Consultar evento |
| PUT | `/api/v1/eventos/{id}/` | Actualizar evento |
| PATCH | `/api/v1/eventos/{id}/` | Actualizar parcialmente |
| DELETE | `/api/v1/eventos/{id}/` | Eliminacion logica |
| GET | `/api/v1/eventos/exportar-csv/` | Exportar registros a CSV |

### Asistentes

| Metodo | Ruta | Descripcion |
|---|---|---|
| GET | `/api/v1/asistentes/` | Listar asistentes activos |
| POST | `/api/v1/asistentes/` | Crear asistente |
| GET | `/api/v1/asistentes/{id}/` | Consultar asistente |
| PUT | `/api/v1/asistentes/{id}/` | Actualizar asistente |
| PATCH | `/api/v1/asistentes/{id}/` | Actualizar parcialmente |
| DELETE | `/api/v1/asistentes/{id}/` | Eliminacion logica |
| GET | `/api/v1/asistentes/exportar-csv/` | Exportar registros a CSV |

### Inscripciones

| Metodo | Ruta | Descripcion |
|---|---|---|
| GET | `/api/v1/inscripciones/` | Listar inscripciones activas |
| POST | `/api/v1/inscripciones/` | Crear inscripcion |
| GET | `/api/v1/inscripciones/{id}/` | Consultar inscripcion |
| PUT | `/api/v1/inscripciones/{id}/` | Actualizar inscripcion |
| PATCH | `/api/v1/inscripciones/{id}/` | Actualizar parcialmente |
| DELETE | `/api/v1/inscripciones/{id}/` | Eliminacion logica |
| GET | `/api/v1/inscripciones/exportar-csv/` | Exportar registros a CSV |

### Pagos

| Metodo | Ruta | Descripcion |
|---|---|---|
| GET | `/api/v1/pagos/` | Listar pagos activos |
| POST | `/api/v1/pagos/` | Crear pago |
| GET | `/api/v1/pagos/{id}/` | Consultar pago |
| PUT | `/api/v1/pagos/{id}/` | Actualizar pago |
| PATCH | `/api/v1/pagos/{id}/` | Actualizar parcialmente |
| DELETE | `/api/v1/pagos/{id}/` | Eliminacion logica |
| GET | `/api/v1/pagos/exportar-csv/` | Exportar registros a CSV |

### Conferencias

| Metodo | Ruta | Descripcion |
|---|---|---|
| GET | `/api/v1/conferencias/` | Listar conferencias activas |
| POST | `/api/v1/conferencias/` | Crear conferencia |
| GET | `/api/v1/conferencias/{id}/` | Consultar conferencia |
| PUT | `/api/v1/conferencias/{id}/` | Actualizar conferencia |
| PATCH | `/api/v1/conferencias/{id}/` | Actualizar parcialmente |
| DELETE | `/api/v1/conferencias/{id}/` | Eliminacion logica |
| GET | `/api/v1/conferencias/exportar-csv/` | Exportar registros a CSV |

### Patrocinadores

| Metodo | Ruta | Descripcion |
|---|---|---|
| GET | `/api/v1/patrocinadores/` | Listar patrocinadores activos |
| POST | `/api/v1/patrocinadores/` | Crear patrocinador |
| GET | `/api/v1/patrocinadores/{id}/` | Consultar patrocinador |
| PUT | `/api/v1/patrocinadores/{id}/` | Actualizar patrocinador |
| PATCH | `/api/v1/patrocinadores/{id}/` | Actualizar parcialmente |
| DELETE | `/api/v1/patrocinadores/{id}/` | Eliminacion logica |
| GET | `/api/v1/patrocinadores/exportar-csv/` | Exportar registros a CSV |

---

## Filtros, Busqueda y Ordenamiento

Todos los endpoints soportan los siguientes parametros de consulta:

Filtrar por campo especifico
GET /api/v1/sedes/?ciudad=Bogota
GET /api/v1/asistentes/?nombre=Angel
GET /api/v1/pagos/?estado=Aprobado
Busqueda de texto en campos de texto
GET /api/v1/sedes/?search=bogota
Ordenamiento ascendente o descendente
GET /api/v1/eventos/?ordering=-fecha_creacion
GET /api/v1/sedes/?ordering=nombre
Incluir registros con soft delete
GET /api/v1/sedes/?incluir_inactivos=true
Paginacion
GET /api/v1/sedes/?page=1&page_size=10

---

## Estructura del Proyecto

```
proyecto/
│
├── api/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── filters.py
│   ├── pagination.py
│   ├── responses.py
│   ├── logging_mixins.py
│   └── auth_views.py
│
├── backend/
│   ├── settings.py
│   └── urls.py
│
├── logs/
│   └── operations.log
│
├── docs/
├── evidencias/
├── .env
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── manage.py
```

## Caracteristicas Implementadas

| N. | Caracteristica | Estado |
|---|---|---|
| 1 | Swagger para documentacion | Implementado |
| 2 | Versionado de API | Implementado |
| 3 | Respuestas JSON estandarizadas | Implementado |
| 4 | Paginacion | Implementado |
| 5 | Filtros por campo | Implementado |
| 6 | Ordenamiento | Implementado |
| 7 | Soft Delete | Implementado |
| 8 | Auditoria de registros | Implementado |
| 9 | Autenticacion JWT | Implementado |
| 10 | Roles y permisos | Implementado |
| 11 | Relaciones anidadas (Nested Serializers) | Implementado |
| 12 | Exportacion CSV | Implementado |
| 13 | Logging de operaciones | Implementado |

---

## Archivo .gitignore

Se creo automaticamente al crear el repositorio en GitHub en la opcion visual studio