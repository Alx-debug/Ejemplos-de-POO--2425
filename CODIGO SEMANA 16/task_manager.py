from task import Task

class TaskManager:
    def __init__(self):
        """
        Inicializa el gestor de tareas con una lista vacía
        """
        self.tareas = []

    def agregar_tarea(self, texto):
        """
        Agrega una nueva tarea a la lista
        Args:
            texto (str): El texto de la tarea a agregar
        """
        nueva_tarea = Task(texto)
        self.tareas.append(nueva_tarea)
        return True

    def completar_tarea(self, indice):
        """
        Marca una tarea como completada
        Args:
            indice (int): El índice de la tarea a completar
        Returns:
            bool: True si se completó la operación, False si el índice es inválido
        """
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completar()
            return True
        return False

    def eliminar_tarea(self, indice):
        """
        Elimina una tarea de la lista
        Args:
            indice (int): El índice de la tarea a eliminar
        Returns:
            bool: True si se eliminó la tarea, False si el índice es inválido
        """
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
            return True
        return False

    def obtener_tareas(self):
        """
        Obtiene la lista de todas las tareas
        Returns:
            list: Lista de objetos Task
        """
        return self.tareas

    def obtener_tarea(self, indice):
        """
        Obtiene una tarea específica
        Args:
            indice (int): El índice de la tarea
        Returns:
            Task: La tarea en el índice especificado o None si el índice es inválido
        """
        if 0 <= indice < len(self.tareas):
            return self.tareas[indice]
        return None

    def total_tareas(self):
        """
        Obtiene el número total de tareas
        Returns:
            int: Número total de tareas
        """
        return len(self.tareas)

    def tareas_completadas(self):
        """
        Obtiene el número de tareas completadas
        Returns:
            int: Número de tareas completadas
        """
        return sum(1 for tarea in self.tareas if tarea.completada)

    def tareas_pendientes(self):
        """
        Obtiene el número de tareas pendientes
        Returns:
            int: Número de tareas pendientes
        """
        return sum(1 for tarea in self.tareas if not tarea.completada)

    def limpiar_completadas(self):
        """
        Elimina todas las tareas completadas
        Returns:
            int: Número de tareas eliminadas
        """
        tareas_anteriores = len(self.tareas)
        self.tareas = [tarea for tarea in self.tareas if not tarea.completada]
        return tareas_anteriores - len(self.tareas)

    def existe_tarea(self, texto):
        """
        Verifica si ya existe una tarea con el mismo texto
        Args:
            texto (str): El texto a buscar
        Returns:
            bool: True si existe una tarea con ese texto, False en caso contrario
        """
        return any(tarea.texto.lower() == texto.lower() for tarea in self.tareas)
