def ingresar_temperaturas():
    """Función para ingresar temperaturas diarias."""
    # Simulación de entrada de datos
    temperaturas = [20.5, 22.3, 19.8, 21.0, 23.1, 18.7, 20.0]  # Datos de ejemplo
    return temperaturas

def calcular_promedio_semanal(temperaturas):
    """Función para calcular el promedio semanal de temperaturas."""
    return sum(temperaturas) / len(temperaturas)

def main():
    """Función principal para ejecutar el programa."""
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio_semanal(temperaturas)
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}")

# Ejecutar el programa
if __name__ == "__main__":
    main()
# ingresar_temperaturas(): Simula la entrada de datos diarios de temperatura.
# calcular_promedio_semanal(): Calcula el promedio de las temperaturas ingresadas.
# main(): Función principal que coordina la ejecución del programa.