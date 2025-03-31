from dataclasses import dataclass
from datetime import datetime

@dataclass
class Evento:
    fecha: str
    hora: str
    descripcion: str
    categoria: str
    prioridad: str

    @property
    def fecha_hora(self) -> datetime:
        return datetime.strptime(f"{self.fecha} {self.hora}",
                               "%d/%m/%Y %H:%M")

    def to_dict(self):
        return {
            "fecha": self.fecha,
            "hora": self.hora,
            "descripcion": self.descripcion,
            "categoria": self.categoria,
            "prioridad": self.prioridad
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            fecha=data["fecha"],
            hora=data["hora"],
            descripcion=data["descripcion"],
            categoria=data["categoria"],
            prioridad=data["prioridad"]
        )