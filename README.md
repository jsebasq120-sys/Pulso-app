# ⚽ Pulso - Sistema de Monitoreo de Fútbol (Pulso Fit)

**Asignatura:** Arquitectura de Software  
**Institución:** Universidad Manuela Beltrán  
**Metodología:** Aprendizaje Basado en Proyectos (ABP)  

---

## 1. Descripción del Proyecto
**Pulso** es una aplicación web full-stack diseñada para la gestión integral y el monitoreo de la condición física de planteles de fútbol. El sistema permite registrar fichajes de jugadores, llevar un control biométrico diario (frecuencia cardíaca, nivel de fatiga, velocidad máxima), almacenar pruebas físicas semanales y registrar eventos o anotaciones en partidos, ofreciendo analítica en tiempo real para el cuerpo técnico.

---

## 2. Arquitectura del Software
El proyecto implementa una **arquitectura en capas (Layered Architecture)**, separando de forma clara las responsabilidades de cada componente para garantizar mantenibilidad, escalabilidad y desacoplamiento:

* **Frontend (`/frontend/`)**: Capa de presentación desarrollada con HTML5, CSS3 personalizado (estética deportiva de alto rendimiento inspirada en *Smart Fit* con tonos oscuros e interacciones en amarillo vibrante) y JavaScript nativo modular (`models.js`, `controllers.js`, `app.js`) para consumir la API REST.
* **Backend (`/backend/`)**: Capa de lógica de negocio y servicios construida con **FastAPI** (Python), encargada de procesar peticiones, validar esquemas con Pydantic, gestionar excepciones y comunicarse con la base de datos.
* **Base de Datos (`/database/`)**: Capa de persistencia implementada en **SQL Server**, estructurada mediante tablas relacionales normalizadas para almacenar la información de usuarios, jugadores, mediciones y pruebas.
* **Comunicación**: Intercambio de información asíncrono basado en protocolo HTTP/REST mediante JSON y CORS habilitado para la integración segura entre el cliente y el servidor.

---

## 3. Estructura del Repositorio
```text
pulso-app/
│
├── backend/
│   ├── venv/
│   ├── app.py             # Servidor FastAPI y endpoints REST
│   ├── database.py        # Conexión ODBC con SQL Server
│   ├── models.py          # Esquemas de validación Pydantic
│   └── requirements.txt   # Dependencias de Python
│
├── database/
│   ├── schema.sql         # Script DDL para creación de BD y tablas
│   └── seed_data.sql      # Datos iniciales de prueba (Seed Data)
│
├── frontend/
│   ├── css/
│   │   └── style.css      # Estilos visuales profesionales (Estética Smart Fit)
│   ├── js/
│   │   ├── app.js         # Punto de entrada principal del frontend
│   │   ├── controllers.js # Lógica de eventos y actualización de vistas
│   │   └── models.js      # Capa de comunicación asíncrona (fetch API)
│   └── index.html         # Interfaz de usuario (Dashboard)
│
├── tests/
│   └── integration_tests.md # Documentación de pruebas de integración
│
├── .gitignore
└── README.md
4. Tecnologías UtilizadasFrontend: HTML5, CSS3, JavaScript (ES6+).Backend: Python 3.x, FastAPI, Uvicorn, Pydantic, pyodbc.Base de Datos: Microsoft SQL Server (SQL Server Management Studio - SSMS).Control de Versiones: Git y GitHub.5. Pruebas de IntegraciónA continuación se documentan las pruebas realizadas para comprobar el flujo completo de la aplicación:Escenario de PruebaResultado EsperadoResultado ObtenidoEstado1. Registro de datosIngresar un nuevo jugador desde la interfaz y verificar que se almacene en SQL Server.El jugador se inserta correctamente en la tabla JUGADOR y se refleja de inmediato en la base de datos.Aprobado2. Consulta de informaciónCargar el dashboard y visualizar en tablas el plantel, mediciones y pruebas físicas.Las tablas del frontend renderizan dinámicamente los registros obtenidos mediante la API.Aprobado3. Datos inválidosEnviar un formulario con campos vacíos o tipos de datos erróneos (ej. texto en edad).FastAPI valida el esquema y bloquea la solicitud retornando un error HTTP 422 Unprocessable Entity.Aprobado4. Error de comunicaciónSimular desconexión deteniendo el servidor backend y realizar una petición web.El sistema captura la excepción de red en consola y alerta al usuario sobre la falla de comunicación.Aprobado6. Instrucciones de Configuración y EjecuciónPrerrequisitosTener instalado Python y SQL Server.Tener instalado un entorno de desarrollo como Visual Studio Code.Paso 1: Configurar la Base de DatosAbre SQL Server Management Studio (SSMS).Ejecuta el script ubicado en database/schema.sql para crear la base de datos pulso_db y sus tablas.Ejecuta el script ubicado en database/seed_data.sql para poblar los datos iniciales de prueba.Paso 2: Iniciar el BackendAbre tu terminal en la carpeta raíz del proyecto y entra al directorio backend:Bashcd backend
Activa el entorno virtual (si aplica) e instala las dependencias:Bashpip install -r requirements.txt
Ejecuta el servidor con Uvicorn:Bashuvicorn app:app --reload
(El servidor correrá en http://127.0.0.1:8000)Paso 3: Iniciar el FrontendAbre la carpeta frontend/ en Visual Studio Code.Abre el archivo index.html utilizando la extensión Live Server.¡Listo! Interactúa con los formularios y el panel de control en tiempo real.