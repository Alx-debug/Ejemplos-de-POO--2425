from typing import Dict, List, Set, Tuple
from datetime import datetime

class Libro:
    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str):
        # Usando tupla para datos inmutables
        self._datos_inmutables = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn
        self.prestado = False

    @property
    def titulo(self) -> str:
        return self._datos_inmutables[0]

    @property
    def autor(self) -> str:
        return self._datos_inmutables[1]

    def __str__(self) -> str:
        estado = "Prestado" if self.prestado else "Disponible"
        return f"Título: {self.titulo}, Autor: {self.autor}, Categoría: {self.categoria}, ISBN: {self.isbn}, Estado: {estado}"

class Usuario:
    def __init__(self, nombre: str, id_usuario: str):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados: List[Libro] = []

    def __str__(self) -> str:
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {len(self.libros_prestados)}"

class Biblioteca:
    def __init__(self):
        # Diccionario para almacenar libros con ISBN como clave
        self.libros: Dict[str, Libro] = {}
        # Conjunto para IDs de usuario únicos
        self.usuarios: Set[str] = set()
        # Diccionario para mapear ID de usuario a objeto Usuario
        self.registro_usuarios: Dict[str, Usuario] = {}
        # Historial de préstamos
        self.historial_prestamos: List[Dict] = []

    def agregar_libro(self, libro: Libro) -> bool:
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            return True
        return False

    def quitar_libro(self, isbn: str) -> bool:
        if isbn in self.libros and not self.libros[isbn].prestado:
            del self.libros[isbn]
            return True
        return False

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)
            self.registro_usuarios[usuario.id_usuario] = usuario
            return True
        return False

    def dar_baja_usuario(self, id_usuario: str) -> bool:
        if id_usuario in self.usuarios:
            usuario = self.registro_usuarios[id_usuario]
            if not usuario.libros_prestados:
                self.usuarios.remove(id_usuario)
                del self.registro_usuarios[id_usuario]
                return True
        return False

    def prestar_libro(self, isbn: str, id_usuario: str) -> bool:
        if (isbn in self.libros and
            id_usuario in self.usuarios and
            not self.libros[isbn].prestado):

            libro = self.libros[isbn]
            usuario = self.registro_usuarios[id_usuario]

            libro.prestado = True
            usuario.libros_prestados.append(libro)

            # Registrar en el historial
            self.historial_prestamos.append({
                'libro': libro,
                'usuario': usuario,
                'fecha_prestamo': datetime.now(),
                'tipo': 'prestamo'
            })
            return True
        return False

    def devolver_libro(self, isbn: str, id_usuario: str) -> bool:
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.registro_usuarios[id_usuario]

            if libro in usuario.libros_prestados:
                libro.prestado = False
                usuario.libros_prestados.remove(libro)

                # Registrar en el historial
                self.historial_prestamos.append({
                    'libro': libro,
                    'usuario': usuario,
                    'fecha_devolucion': datetime.now(),
                    'tipo': 'devolucion'
                })
                return True
        return False

    def buscar_libros(self, criterio: str, valor: str) -> List[Libro]:
        resultados = []
        for libro in self.libros.values():
            if criterio.lower() == 'titulo' and valor.lower() in libro.titulo.lower():
                resultados.append(libro)
            elif criterio.lower() == 'autor' and valor.lower() in libro.autor.lower():
                resultados.append(libro)
            elif criterio.lower() == 'categoria' and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario: str) -> List[Libro]:
        if id_usuario in self.usuarios:
            return self.registro_usuarios[id_usuario].libros_prestados
        return []

# Código de prueba
def main():
    # Crear una instancia de la biblioteca
    biblioteca = Biblioteca()

    # Crear algunos libros
    libro1 = Libro("Don Quijote", "Miguel de Cervantes", "Clásico", "ISBN001")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", "ISBN002")
    libro3 = Libro("El principito", "Antoine de Saint-Exupéry", "Infantil", "ISBN003")

    # Agregar libros a la biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # Crear y registrar usuarios
    usuario1 = Usuario("Juan Pérez", "U001")
    usuario2 = Usuario("María García", "U002")

    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Realizar algunas operaciones
    print("\nBúsqueda de libros por categoría 'Ficción':")
    for libro in biblioteca.buscar_libros('categoria', 'Ficción'):
        print(libro)

    print("\nPrestando libro a usuario:")
    if biblioteca.prestar_libro("ISBN001", "U001"):
        print("Libro prestado exitosamente")

    print("\nLibros prestados a Juan Pérez:")
    for libro in biblioteca.listar_libros_prestados("U001"):
        print(libro)

    print("\nDevolviendo libro:")
    if biblioteca.devolver_libro("ISBN001", "U001"):
        print("Libro devuelto exitosamente")

if __name__ == "__main__":
    main()