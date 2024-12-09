class Estudiante:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        self.__calificaciones = []

    def agregar_calificacion(self, calificacion):
        if 0 <= calificacion <= 10:
            self.__calificaciones.append(calificacion)
        else:
            print("Calificación inválida")

    def obtener_promedio(self):
        if len(self.__calificaciones) > 0:
            return sum(self.__calificaciones) / len(self.__calificaciones)
        return 0

    def obtener_info(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}, Promedio: {self.obtener_promedio():.2f}"

# Uso
estudiante = Estudiante("Ana", 20)
estudiante.agregar_calificacion(8.5)
estudiante.agregar_calificacion(9.0)
estudiante.agregar_calificacion(7.5)

print(estudiante.obtener_info())