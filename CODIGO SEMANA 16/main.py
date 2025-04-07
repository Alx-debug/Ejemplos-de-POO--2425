from todo_app import TodoApp
import tkinter as tk

def main():
    # Crear la ventana principal
    root = tk.Tk()

    # Crear una instancia de la aplicación
    app = TodoApp(root)

    # Iniciar el bucle principal de la aplicación
    root.mainloop()

# Punto de entrada del programa
if __name__ == "__main__":
    main()
