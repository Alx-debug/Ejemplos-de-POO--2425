class ClimaDiario:
    """Clase que representa la información diaria del clima."""
    def __init__(self, temperaturas):
        self.temperaturas = temperaturas  # Lista de temperaturas diarias

    def calcular_promedio_semanal(self):
        """Método para calcular el promedio semanal de temperaturas."""
        return sum(self.temperaturas) / len(self.temperaturas)

def main():
    """Función principal para ejecutar el programa."""
    # Simulación de entrada de datos
    temperaturas = [20.5, 22.3, 19.8, 21.0, 23.1, 18.7, 20.0]  # Datos de ejemplo
    clima = ClimaDiario(temperaturas)
    promedio = clima.calcular_promedio_semanal()
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}")

# Ejecutar el programa
if __name__ == "__main__":
    main()
"""En esta implementación, hemos creado una clase ClimaDiario que encapsula la información y el comportamiento relacionados con el clima diario. La clase tiene un método calcular_promedio_semanal() que realiza el cálculo del promedio."""