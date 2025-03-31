from src.models.tarea import Tarea

class GestorTareas:
    """
    Clase que maneja la lógica de negocio para las tareas.
    """
    def __init__(self):
        self.tareas = []
        self.observadores = []

    def agregar_observador(self, observador):
        """Añade un observador para notificar cambios."""
        self.observadores.append(observador)

    def notificar_observadores(self):
        """Notifica a todos los observadores sobre cambios."""
        for observador in self.observadores:
            observador()

    def agregar_tarea(self, texto_tarea):
        """Agrega una nueva tarea a la lista."""
        if not texto_tarea.strip():
            return False
        nueva_tarea = Tarea(texto_tarea)
        self.tareas.append(nueva_tarea)
        self.notificar_observadores()
        return True

    def eliminar_tarea(self, indice):
        """Elimina una tarea de la lista."""
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
            self.notificar_observadores()
            return True
        return False

    def marcar_completada(self, indice):
        """Marca una tarea como completada."""
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].marcar_completada()
            self.notificar_observadores()
            return True
        return False

    def obtener_tareas(self):
        """Retorna la lista actual de tareas."""
        return self.tareas
