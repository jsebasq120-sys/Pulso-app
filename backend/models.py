from pydantic import BaseModel
from typing import Optional

class Jugador(BaseModel):
    nombre: str
    posicion: str
    edad: int
    numero_camiseta: int
    usuario_id: Optional[int] = 1