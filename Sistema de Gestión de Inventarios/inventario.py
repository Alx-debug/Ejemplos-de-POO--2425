# inventario.py
from product import Producto


class Inventario:
    """Clase que gestiona la colección de productos"""

    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto: Producto):
        """Añade un nuevo producto verificando ID único"""
        if any(p.id == producto.id for p in self._productos):
            raise ValueError("Error: El ID ya existe")
        self._productos.append(producto)

    def eliminar_producto(self, id: int):
        """Elimina un producto por ID"""
        producto = next((p for p in self._productos if p.id == id), None)
        if producto:
            self._productos.remove(producto)
            return True
        return False

    def actualizar_producto(self, id: int, **kwargs):
        """Actualiza propiedades de un producto"""
        producto = next((p for p in self._productos if p.id == id), None)
        if not producto:
            raise ValueError("Producto no encontrado")

        for key, value in kwargs.items():
            if hasattr(producto, key):
                setattr(producto, key, value)

    def buscar_por_nombre(self, nombre: str):
        """Busca productos por coincidencia parcial en el nombre"""
        return [p for p in self._productos if nombre.lower() in p.nombre.lower()]

    def mostrar_inventario(self):
        """Muestra todos los productos en formato tabular"""
        if not self._productos:
            print("Inventario vacío")
            return

        print("\n{:<5} {:<20} {:<10} {:<10}".format(
            'ID', 'Nombre', 'Stock', 'Precio'))
        for p in self._productos:
            print("{:<5} {:<20} {:<10} {:<10.2f}".format(
                p.id, p.nombre, p.cantidad, p.precio))
        print()
