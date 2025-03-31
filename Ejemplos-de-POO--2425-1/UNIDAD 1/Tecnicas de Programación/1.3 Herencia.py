class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}"

class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, garantia):
        super().__init__(nombre, precio)
        self.garantia = garantia

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Garantía: {self.garantia} meses"

class ProductoAlimenticio(Producto):
    def __init__(self, nombre, precio, fecha_caducidad):
        super().__init__(nombre, precio)
        self.fecha_caducidad = fecha_caducidad

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Caduca: {self.fecha_caducidad}"

# Uso
telefono = ProductoElectronico("Smartphone", 599.99, 12)
manzana = ProductoAlimenticio("Manzana", 0.5, "2024-12-31")

print(telefono.mostrar_info())
print(manzana.mostrar_info())