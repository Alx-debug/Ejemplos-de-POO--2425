class RecursoImportante:
    def __init__(self, nombre, valor):
        """
        Constructor de la clase RecursoImportante.
        Se llama automáticamente al crear una nueva instancia.
        Inicializa los atributos del objeto y simula la apertura de un recurso.
        """
        self.nombre = nombre
        self.valor = valor
        self.recurso_abierto = True
        print(f"Constructor: Inicializando RecursoImportante '{self.nombre}' con valor {self.valor}")
        print(f"Constructor: Recurso '{self.nombre}' abierto")

    def __del__(self):
        """
        Destructor de la clase RecursoImportante.
        Se llama automáticamente cuando el objeto está a punto de ser destruido.
        Simula el cierre del recurso si aún está abierto.
        """
        if self.recurso_abierto:
            print(f"Destructor: Cerrando recurso '{self.nombre}'")
            self.recurso_abierto = False
        print(f"Destructor: Objeto RecursoImportante '{self.nombre}' está siendo destruido")

    def usar_recurso(self):
        """
        Método que simula el uso del recurso.
        """
        if self.recurso_abierto:
            print(f"Usando el recurso '{self.nombre}' con valor {self.valor}")
        else:
            print(f"Error: El recurso '{self.nombre}' está cerrado")

    def cerrar_recurso(self):
        """
        Método para cerrar manualmente el recurso.
        """
        if self.recurso_abierto:
            print(f"Cerrando manualmente el recurso '{self.nombre}'")
            self.recurso_abierto = False
        else:
            print(f"El recurso '{self.nombre}' ya está cerrado")


# Demostración del uso de la clase
if __name__ == "__main__":
    print("Creando instancia de RecursoImportante")
    recurso = RecursoImportante("Archivo1", 42)

    print("\nUsando el recurso")
    recurso.usar_recurso()

    print("\nCerrando el recurso manualmente")
    recurso.cerrar_recurso()

    print("\nIntentando usar el recurso después de cerrarlo")
    recurso.usar_recurso()

    print("\nEl programa principal ha terminado. El destructor se llamará automáticamente.")
