# Este programa calcula el área de diferentes figuras geométricas (círculo, triángulo, rectángulo)
# y permite al usuario elegir la figura deseada.

import math

def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    return math.pi * radio ** 2

def calcular_area_triangulo(base, altura):
    """Calcula el área de un triángulo dada su base y altura."""
    return 0.5 * base * altura

def calcular_area_rectangulo(largo, ancho):
    """Calcula el área de un rectángulo dado su largo y ancho."""
    return largo * ancho

def obtener_numero(mensaje):
    """Solicita al usuario un número y lo devuelve como float."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Menú principal
print("Calculadora de Áreas")
print("1. Círculo")
print("2. Triángulo")
print("3. Rectángulo")

opcion = input("Seleccione la figura (1/2/3): ")

if opcion == "1":
    radio = obtener_numero("Ingrese el radio del círculo: ")
    area = calcular_area_circulo(radio)
    print(f"El área del círculo es: {area:.2f}")
elif opcion == "2":
    base = obtener_numero("Ingrese la base del triángulo: ")
    altura = obtener_numero("Ingrese la altura del triángulo: ")
    area = calcular_area_triangulo(base, altura)
    print(f"El área del triángulo es: {area:.2f}")
elif opcion == "3":
    largo = obtener_numero("Ingrese el largo del rectángulo: ")
    ancho = obtener_numero("Ingrese el ancho del rectángulo: ")
    area = calcular_area_rectangulo(largo, ancho)
    print(f"El área del rectángulo es: {area:.2f}")
else:
    print("Opción no válida.")

# Variable booleana para demostrar el uso de este tipo de dato
calculo_exitoso = opcion in ["1", "2", "3"]

if calculo_exitoso:
    print("Cálculo realizado con éxito.")
else:
    print("No se pudo realizar el cálculo.")
