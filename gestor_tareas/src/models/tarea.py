from datetime import datetime

class Tarea:
    """
    Clase que representa una tarea individual.
    """
    def __init__(self, texto):
        self.texto = texto
        self.completada = False
        self.fecha_creacion = datetime.now()
        self.fecha_completado = None

    def marcar_completada(self):
        """Marca la tarea como completada."""
        self.completada = True
        self.fecha_completado = datetime.now()

    def __str__(self):
        """Representación en string de la tarea."""
        return f"{'✓' if self.completada else '•'} {self.texto}"