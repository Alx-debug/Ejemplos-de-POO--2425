<<<<<<< HEAD
# inventario.py
from product import Producto
import os

class Inventario:
    """Clase que gestiona la colección de productos con persistencia en archivo"""
    
    ARCHIVO = "inventario.txt"
    
    def __init__(self):
        self._productos = []
        self._cargar_inventario()  # Carga inicial desde el archivo
    
    def _cargar_inventario(self):
        """Carga los productos desde el archivo"""
        try:
            # Crear el archivo si no existe
            if not os.path.exists(self.ARCHIVO):
                with open(self.ARCHIVO, 'w', encoding='utf-8'):
                    pass  # Archivo creado vacío
            
            with open(self.ARCHIVO, 'r', encoding='utf-8') as f:
                for linea in f:
                    linea = linea.strip()
                    if not linea:
                        continue  # Ignorar líneas vacías
                    try:
                        id_str, nombre, cantidad_str, precio_str = linea.split(',')
                        producto = Producto(
                            id=int(id_str),
                            nombre=nombre,
                            cantidad=int(cantidad_str),
                            precio=float(precio_str)
                        )
                        self._productos.append(producto)
                    except (ValueError, IndexError) as e:
                        print(f"Error en línea corrupta: '{linea}' - {str(e)}")
        except PermissionError:
            raise PermissionError("Error: Sin permisos para leer el archivo")
        except Exception as e:
            raise RuntimeError(f"Error al cargar el inventario: {str(e)}")

    def _guardar_inventario(self):
        """Guarda todos los productos en el archivo"""
        try:
            with open(self.ARCHIVO, 'w', encoding='utf-8') as f:
                for producto in self._productos:
                    linea = f"{producto.id},{producto.nombre},{producto.cantidad},{producto.precio}\n"
                    f.write(linea)
        except PermissionError:
            raise PermissionError("Error: Sin permisos para escribir en el archivo")
        except Exception as e:
            raise RuntimeError(f"Error al guardar el inventario: {str(e)}")

    # Resto de métodos (agregar_producto, eliminar_producto, etc.) igual que antes
    
    def agregar_producto(self, producto: Producto):
        """Añade un producto verificando ID único y guarda en archivo"""
        if any(p.id == producto.id for p in self._productos):
            raise ValueError(f"ID {producto.id} ya existe")
        self._productos.append(producto)
        self._guardar_inventario()
    
    def eliminar_producto(self, id: int):
        """Elimina un producto por ID y actualiza el archivo"""
        producto = next((p for p in self._productos if p.id == id), None)
        if producto:
            self._productos.remove(producto)
            self._guardar_inventario()
            return True
        return False
    
    def actualizar_producto(self, id: int, **kwargs):
        """Actualiza propiedades de un producto y guarda cambios"""
        producto = next((p for p in self._productos if p.id == id), None)
        if not producto:
            raise ValueError("Producto no encontrado")
        
        for clave, valor in kwargs.items():
            if hasattr(producto, clave):
                setattr(producto, clave, valor)
        
        self._guardar_inventario()
    
    def buscar_por_nombre(self, nombre: str):
        """Busca productos por coincidencia parcial en el nombre"""
        return [p for p in self._productos if nombre.lower() in p.nombre.lower()]
    
    def mostrar_inventario(self):
        """Muestra todos los productos en formato tabular"""
        if not self._productos:
            print("\nInventario vacío")
            return
        
        print("\n{:<5} {:<25} {:<10} {:<10}".format(
            'ID', 'NOMBRE', 'STOCK', 'PRECIO'))
        for producto in self._productos:
            print("{:<5} {:<25} {:<10} ${:<9.2f}".format(
                producto.id,
                producto.nombre[:24],  # Limita el nombre a 24 caracteres
                producto.cantidad,
                producto.precio
            ))
=======
# inventario.py
from product import Producto
import os

class Inventario:
    """Clase que gestiona la colección de productos con persistencia en archivo"""
    
    ARCHIVO = "inventario.txt"
    
    def __init__(self):
        self._productos = []
        self._cargar_inventario()  # Carga inicial desde el archivo
    
    def _cargar_inventario(self):
        """Carga los productos desde el archivo"""
        try:
            # Crear el archivo si no existe
            if not os.path.exists(self.ARCHIVO):
                with open(self.ARCHIVO, 'w', encoding='utf-8'):
                    pass  # Archivo creado vacío
            
            with open(self.ARCHIVO, 'r', encoding='utf-8') as f:
                for linea in f:
                    linea = linea.strip()
                    if not linea:
                        continue  # Ignorar líneas vacías
                    try:
                        id_str, nombre, cantidad_str, precio_str = linea.split(',')
                        producto = Producto(
                            id=int(id_str),
                            nombre=nombre,
                            cantidad=int(cantidad_str),
                            precio=float(precio_str)
                        )
                        self._productos.append(producto)
                    except (ValueError, IndexError) as e:
                        print(f"Error en línea corrupta: '{linea}' - {str(e)}")
        except PermissionError:
            raise PermissionError("Error: Sin permisos para leer el archivo")
        except Exception as e:
            raise RuntimeError(f"Error al cargar el inventario: {str(e)}")

    def _guardar_inventario(self):
        """Guarda todos los productos en el archivo"""
        try:
            with open(self.ARCHIVO, 'w', encoding='utf-8') as f:
                for producto in self._productos:
                    linea = f"{producto.id},{producto.nombre},{producto.cantidad},{producto.precio}\n"
                    f.write(linea)
        except PermissionError:
            raise PermissionError("Error: Sin permisos para escribir en el archivo")
        except Exception as e:
            raise RuntimeError(f"Error al guardar el inventario: {str(e)}")

    # Resto de métodos (agregar_producto, eliminar_producto, etc.) igual que antes
    
    def agregar_producto(self, producto: Producto):
        """Añade un producto verificando ID único y guarda en archivo"""
        if any(p.id == producto.id for p in self._productos):
            raise ValueError(f"ID {producto.id} ya existe")
        self._productos.append(producto)
        self._guardar_inventario()
    
    def eliminar_producto(self, id: int):
        """Elimina un producto por ID y actualiza el archivo"""
        producto = next((p for p in self._productos if p.id == id), None)
        if producto:
            self._productos.remove(producto)
            self._guardar_inventario()
            return True
        return False
    
    def actualizar_producto(self, id: int, **kwargs):
        """Actualiza propiedades de un producto y guarda cambios"""
        producto = next((p for p in self._productos if p.id == id), None)
        if not producto:
            raise ValueError("Producto no encontrado")
        
        for clave, valor in kwargs.items():
            if hasattr(producto, clave):
                setattr(producto, clave, valor)
        
        self._guardar_inventario()
    
    def buscar_por_nombre(self, nombre: str):
        """Busca productos por coincidencia parcial en el nombre"""
        return [p for p in self._productos if nombre.lower() in p.nombre.lower()]
    
    def mostrar_inventario(self):
        """Muestra todos los productos en formato tabular"""
        if not self._productos:
            print("\nInventario vacío")
            return
        
        print("\n{:<5} {:<25} {:<10} {:<10}".format(
            'ID', 'NOMBRE', 'STOCK', 'PRECIO'))
        for producto in self._productos:
            print("{:<5} {:<25} {:<10} ${:<9.2f}".format(
                producto.id,
                producto.nombre[:24],  # Limita el nombre a 24 caracteres
                producto.cantidad,
                producto.precio
            ))
>>>>>>> f0671391667654dc7287141ab6e2bcfce40bb74b
        print(f"\nTotal de productos: {len(self._productos)}\n")