import json
import os
from typing import List
from ..models.evento import Evento

def cargar_eventos(archivo: str) -> List[Evento]:
    if os.path.exists(archivo):
        try:
            with open(archivo, 'r') as f:
                datos = json.load(f)
                return [Evento.from_dict(evento) for evento in datos]
        except:
            return []
    return []

def guardar_eventos(archivo: str, eventos: List[Evento]):
    with open(archivo, 'w') as f:
        json.dump([evento.to_dict() for evento in eventos],
                 f,
                 indent=4)