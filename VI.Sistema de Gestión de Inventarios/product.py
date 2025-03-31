# product.py
class Producto:
    """Clase que representa un producto en el inventario"""

    def __init__(self, id: int, nombre: str, cantidad: int, precio: float):
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Propiedades (getters)
    @property
    def id(self) -> int:
        return self._id

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def cantidad(self) -> int:
        return self._cantidad

    @property
    def precio(self) -> float:
        return self._precio

    # Setters con validación básica
    @nombre.setter
    def nombre(self, valor: str):
        if not valor.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor

    @cantidad.setter
    def cantidad(self, valor: int):
        if valor < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self._cantidad = valor

    @precio.setter
    def precio(self, valor: float):
        if valor <= 0:
            raise ValueError("El precio debe ser mayor a cero")
        self._precio = valor

    def __str__(self) -> str:
        return f"ID: {self._id} | {self._nombre} | Stock: {self._cantidad} | Precio: ${self._precio:.2f}"
