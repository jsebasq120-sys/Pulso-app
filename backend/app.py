from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import get_db_connection
from models import Jugador

app = FastAPI(title="Pulso API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Medicion(BaseModel):
    jugador_id: int
    frecuencia_cardiaca: int
    fatiga_nivel: int
    velocidad_maxima: float

class PruebaFisica(BaseModel):
    jugador_id: int
    tipo_prueba: str
    resultado: float

class Anotacion(BaseModel):
    jugador_id: int
    partido: str
    minuto: int
    descripcion: str

@app.get("/")
def read_root():
    return {"message": "¡Bienvenido al backend de Pulso! ⚽"}

@app.get("/test-db")
def test_database_connection():
    conn = get_db_connection()
    if conn:
        conn.close()
        return {"status": "success", "message": "¡Conexión exitosa a SQL Server desde FastAPI!"}
    return {"status": "error", "message": "No se pudo establecer la conexión con la base de datos."}

# --- JUGADORES ---
@app.get("/jugadores")
def get_jugadores():
    conn = get_db_connection()
    if not conn: return {"error": "Sin conexión"}
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, posicion, edad, numero_camiseta FROM JUGADOR")
    cols = [c[0] for c in cursor.description]
    res = [dict(zip(cols, row)) for row in cursor.fetchall()]
    cursor.close(); conn.close()
    return {"total": len(res), "jugadores": res}

@app.post("/jugadores")
def crear_jugador(jugador: Jugador):
    conn = get_db_connection()
    if not conn: return {"error": "Sin conexión"}
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO JUGADOR (nombre, posicion, edad, numero_camiseta, usuario_id) VALUES (?, ?, ?, ?, ?)", 
                       (jugador.nombre, jugador.posicion, jugador.edad, jugador.numero_camiseta, jugador.usuario_id))
        conn.commit()
        return {"status": "success", "message": f"Jugador {jugador.nombre} creado"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        cursor.close(); conn.close()

# --- MEDICIONES ---
@app.get("/mediciones")
def get_mediciones():
    conn = get_db_connection()
    if not conn: return {"error": "Sin conexión"}
    cursor = conn.cursor()
    cursor.execute("SELECT m.id, j.nombre AS jugador, m.frecuencia_cardiaca, m.fatiga_nivel, m.velocidad_maxima, m.fecha_registro FROM MEDICION m JOIN JUGADOR j ON m.jugador_id = j.id")
    cols = [c[0] for c in cursor.description]
    res = [dict(zip(cols, row)) for row in cursor.fetchall()]
    cursor.close(); conn.close()
    return {"total": len(res), "mediciones": res}

@app.post("/mediciones")
def crear_medicion(medicion: Medicion):
    conn = get_db_connection()
    if not conn: return {"error": "Sin conexión"}
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO MEDICION (jugador_id, frecuencia_cardiaca, fatiga_nivel, velocidad_maxima) VALUES (?, ?, ?, ?)", 
                       (medicion.jugador_id, medicion.frecuencia_cardiaca, medicion.fatiga_nivel, medicion.velocidad_maxima))
        conn.commit()
        return {"status": "success", "message": "Medición registrada"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        cursor.close(); conn.close()

# --- PRUEBAS FISICAS ---
@app.get("/pruebas-fisicas")
def get_pruebas_fisicas():
    conn = get_db_connection()
    if not conn: return {"error": "Sin conexión"}
    cursor = conn.cursor()
    cursor.execute("SELECT p.id, j.nombre AS jugador, p.tipo_prueba, p.resultado, p.fecha FROM PRUEBA_FISICA p JOIN JUGADOR j ON p.jugador_id = j.id")
    cols = [c[0] for c in cursor.description]
    res = [dict(zip(cols, row)) for row in cursor.fetchall()]
    cursor.close(); conn.close()
    return {"total": len(res), "pruebas_fisicas": res}

@app.post("/pruebas-fisicas")
def crear_prueba_fisica(prueba: PruebaFisica):
    conn = get_db_connection()
    if not conn: return {"error": "Sin conexión"}
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO PRUEBA_FISICA (jugador_id, tipo_prueba, resultado) VALUES (?, ?, ?)", 
                       (prueba.jugador_id, prueba.tipo_prueba, prueba.resultado))
        conn.commit()
        return {"status": "success", "message": "Prueba física registrada"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        cursor.close(); conn.close()

# --- ANOTACIONES ---
@app.get("/anotaciones")
def get_anotaciones():
    conn = get_db_connection()
    if not conn: return {"error": "Sin conexión"}
    cursor = conn.cursor()
    cursor.execute("SELECT a.id, j.nombre AS jugador, a.partido, a.minuto, a.descripcion FROM ANOTACION a JOIN JUGADOR j ON a.jugador_id = j.id")
    cols = [c[0] for c in cursor.description]
    res = [dict(zip(cols, row)) for row in cursor.fetchall()]
    cursor.close(); conn.close()
    return {"total": len(res), "anotaciones": res}

@app.post("/anotaciones")
def crear_anotacion(anotacion: Anotacion):
    conn = get_db_connection()
    if not conn: return {"error": "Sin conexión"}
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO ANOTACION (jugador_id, partido, minuto, descripcion) VALUES (?, ?, ?, ?)", 
                       (anotacion.jugador_id, anotacion.partido, anotacion.minuto, anotacion.descripcion))
        conn.commit()
        return {"status": "success", "message": "Anotación registrada"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        cursor.close(); conn.close()