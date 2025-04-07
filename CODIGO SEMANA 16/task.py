from datetime import datetime

class Task:
    """
    Clase que representa una tarea individual
    """
    def __init__(self, texto):
        """
        Inicializa una nueva tarea
        Args:
            texto (str): El texto/descripción de la tarea
        """
        self.texto = texto
        self.completada = False
        self.fecha_creacion = datetime.now()
        self.fecha_completado = None
        self.prioridad = "normal"  # puede ser: "baja", "normal", "alta"

    def completar(self):
        """
        Marca la tarea como completada y registra la fecha
        """
        self.completada = True
        self.fecha_completado = datetime.now()

    def descompletar(self):
        """
        Desmarca la tarea como completada
        """
        self.completada = False
        self.fecha_completado = None

    def establecer_prioridad(self, prioridad):
        """
        Establece la prioridad de la tarea
        Args:
            prioridad (str): "baja", "normal" o "alta"
        """
        if prioridad.lower() in ["baja", "normal", "alta"]:
            self.prioridad = prioridad.lower()

    def obtener_tiempo_creacion(self):
        """
        Obtiene el tiempo transcurrido desde la creación
        Returns:
            str: Tiempo transcurrido en formato legible
        """
        tiempo_transcurrido = datetime.now() - self.fecha_creacion
        return self._formato_tiempo(tiempo_transcurrido)

    def obtener_tiempo_completado(self):
        """
        Obtiene el tiempo transcurrido desde que se completó
        Returns:
            str: Tiempo transcurrido en formato legible o None si no está completada
        """
        if self.fecha_completado:
            tiempo_transcurrido = datetime.now() - self.fecha_completado
            return self._formato_tiempo(tiempo_transcurrido)
        return None

    def _formato_tiempo(self, delta):
        """
        Convierte un timedelta en un formato legible
        Args:
            delta: objeto timedelta
        Returns:
            str: Tiempo en formato legible
        """
        dias = delta.days
        horas = delta.seconds // 3600
        minutos = (delta.seconds % 3600) // 60

        if dias > 0:
            return f"{dias} días"
        elif horas > 0:
            return f"{horas} horas"
        else:
            return f"{minutos} minutos"

    def __str__(self):
        """
        Representación en string de la tarea
        Returns:
            str: Representación de la tarea
        """
        estado = "✓" if self.completada else "□"
        return f"{estado} {self.texto} [{self.prioridad}]"

    def __repr__(self):
        """
        Representación oficial de la tarea
        Returns:
            str: Representación detallada de la tarea
        """
        return f"Task(texto='{self.texto}', completada={self.completada}, prioridad='{self.prioridad}')"

    def to_dict(self):
        """
        Convierte la tarea a un diccionario
        Returns:
            dict: Diccionario con los datos de la tarea
        """
        return {
            'texto': self.texto,
            'completada': self.completada,
            'fecha_creacion': self.fecha_creacion.isoformat(),
            'fecha_completado': self.fecha_completado.isoformat() if self.fecha_completado else None,
            'prioridad': self.prioridad
        }

    @classmethod
    def from_dict(cls, datos):
        """
        Crea una tarea desde un diccionario
        Args:
            datos (dict): Diccionario con los datos de la tarea
        Returns:
            Task: Nueva instancia de Task
        """
        tarea = cls(datos['texto'])
        tarea.completada = datos['completada']
        tarea.fecha_creacion = datetime.fromisoformat(datos['fecha_creacion'])
        if datos['fecha_completado']:
            tarea.fecha_completado = datetime.fromisoformat(datos['fecha_completado'])
        tarea.prioridad = datos['prioridad']
        return tarea
