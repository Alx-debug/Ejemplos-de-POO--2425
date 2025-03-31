class Vehiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca  # Atributo encapsulado
        self.__modelo = modelo  # Atributo encapsulado
        self.__encendido = False

    def encender(self):
        self.__encendido = True
        print(f"{self.__marca} {self.__modelo} encendido.")

    def apagar(self):
        self.__encendido = False
        print(f"{self.__marca} {self.__modelo} apagado.")

    def get_info(self):
        return f"Vehículo: {self.__marca} {self.__modelo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas

    def get_info(self):  # Polimorfismo: sobrescritura de método
        return f"{super().get_info()}, Puertas: {self.num_puertas}"

    def tocar_claxon(self):
        print("¡Beep, beep!")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def get_info(self):  # Polimorfismo: sobrescritura de método
        return f"{super().get_info()}, Tipo: {self.tipo}"

    def hacer_caballito(self):
        print("¡Haciendo un caballito!")

# Creación de instancias
coche1 = Coche("Toyota", "Corolla", 4)
moto1 = Motocicleta("Honda", "CBR", "Deportiva")

# Demostración de funcionalidad
print(coche1.get_info())
coche1.encender()
coche1.tocar_claxon()
coche1.apagar()

print("\n" + moto1.get_info())
moto1.encender()
moto1.hacer_caballito()
moto1.apagar()
