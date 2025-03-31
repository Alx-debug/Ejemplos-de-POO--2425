import os
import sys

# Añade el directorio src al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gui.app import AgendaApp

def main():
    app = AgendaApp()
    app.mainloop()

if __name__ == "__main__":
    main()
    # En app.py
print("Definiendo AgendaApp")
class AgendaApp(tk.Tk):
    def __init__(self):
        print("Inicializando AgendaApp")
        super().__init__()
        # ...

# En main.py
print("Intentando importar AgendaApp")
from gui.app import AgendaApp
print("Importación exitosa")