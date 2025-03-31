class Hotel:
    def __init__(self, nombre, ubicacion):
        # Constructor de la clase Hotel
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.habitaciones = []  # Lista para almacenar las habitaciones del hotel

    def agregar_habitacion(self, habitacion):
        # Método para agregar una habitación al hotel
        self.habitaciones.append(habitacion)

    def mostrar_info(self):
        # Método para mostrar información general del hotel
        return f"Hotel: {self.nombre}, Ubicación: {self.ubicacion}, Habitaciones: {len(self.habitaciones)}"

class Habitacion:
    def __init__(self, numero, tipo, precio):
        # Constructor de la clase Habitación
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True  # Por defecto, la habitación está disponible

    def cambiar_disponibilidad(self):
        # Método para cambiar el estado de disponibilidad de la habitación
        self.disponible = not self.disponible

    def mostrar_info(self):
        # Método para mostrar información detallada de la habitación
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Habitación {self.numero}: {self.tipo}, Precio: ${self.precio}, Estado: {estado}"

class Cliente:
    def __init__(self, nombre, email):
        # Constructor de la clase Cliente
        self.nombre = nombre
        self.email = email
        self.reservas = []  # Lista para almacenar las reservas del cliente

    def realizar_reserva(self, reserva):
        # Método para agregar una reserva al cliente
        self.reservas.append(reserva)

    def mostrar_info(self):
        # Método para mostrar información del cliente
        return f"Cliente: {self.nombre}, Email: {self.email}, Reservas: {len(self.reservas)}"

class Reserva:
    def __init__(self, cliente, habitacion, fecha_entrada, fecha_salida):
        # Constructor de la clase Reserva
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.estado = "Confirmada"
        self.habitacion.cambiar_disponibilidad()  # Marca la habitación como no disponible

    def cancelar_reserva(self):
        # Método para cancelar la reserva
        self.estado = "Cancelada"
        self.habitacion.cambiar_disponibilidad()  # Marca la habitación como disponible nuevamente

    def mostrar_info(self):
        # Método para mostrar información detallada de la reserva
        return f"Reserva: Cliente: {self.cliente.nombre}, Habitación: {self.habitacion.numero}, " \
               f"Entrada: {self.fecha_entrada}, Salida: {self.fecha_salida}, Estado: {self.estado}"

# Ejemplo de uso del sistema de reservas
hotel = Hotel("Hotel Paraíso", "Playa del Carmen")

# Creación de habitaciones
habitacion1 = Habitacion(101, "Individual", 100)
habitacion2 = Habitacion(202, "Doble", 150)

# Agregar habitaciones al hotel
hotel.agregar_habitacion(habitacion1)
hotel.agregar_habitacion(habitacion2)

# Creación de clientes
cliente1 = Cliente("Juan Pérez", "juan@email.com")
cliente2 = Cliente("María García", "maria@email.com")

# Realización de reservas
reserva1 = Reserva(cliente1, habitacion1, "2025-01-15", "2025-01-20")
cliente1.realizar_reserva(reserva1)

reserva2 = Reserva(cliente2, habitacion2, "2025-02-01", "2025-02-05")
cliente2.realizar_reserva(reserva2)

# Mostrar información del sistema
print(hotel.mostrar_info())
print(habitacion1.mostrar_info())
print(habitacion2.mostrar_info())
print(cliente1.mostrar_info())
print(cliente2.mostrar_info())
print(reserva1.mostrar_info())
print(reserva2.mostrar_info())

# Cancelar una reserva y mostrar los cambios
reserva1.cancelar_reserva()
print(reserva1.mostrar_info())
print(habitacion1.mostrar_info())

