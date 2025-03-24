import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Asegúrate de tener instalado tkcalendar

class AgendaApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Agenda Personal")
        self.geometry("400x600")

        # Lista para almacenar las tareas
        self.tareas = []

        # Crear widgets de la interfaz
        self.crear_widgets()

    def crear_widgets(self):
        # Etiqueta y entrada para el título
        tk.Label(self, text="Título:").pack(pady=5)
        self.titulo_entry = tk.Entry(self, width=40)
        self.titulo_entry.pack(pady=5)

        # Selector de fecha
        tk.Label(self, text="Fecha:").pack(pady=5)
        self.fecha_entry = DateEntry(self, width=37, background="darkblue", foreground="white", date_pattern="dd/MM/yyyy")
        self.fecha_entry.pack(pady=5)

        # Área de texto para la descripción
        tk.Label(self, text="Descripción:").pack(pady=5)
        self.descripcion_text = tk.Text(self, width=40, height=5)
        self.descripcion_text.pack(pady=5)

        # Botón para agregar tarea
        tk.Button(self, text="Agregar Tarea", command=self.agregar_tarea).pack(pady=10)

        # Lista de tareas
        tk.Label(self, text="Tareas:").pack(pady=5)
        self.lista_tareas = tk.Listbox(self, width=50, height=15)
        self.lista_tareas.pack(pady=5)

        # Botón para ver detalles de la tarea seleccionada
        tk.Button(self, text="Ver Detalles", command=self.ver_detalles).pack(pady=5)

    def agregar_tarea(self):
        # Obtener datos de los campos
        titulo = self.titulo_entry.get()
        fecha = self.fecha_entry.get()
        descripcion = self.descripcion_text.get("1.0", tk.END).strip()

        # Validar que los campos no estén vacíos
        if not titulo or not fecha or not descripcion:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")
            return

        # Agregar tarea a la lista
        tarea = {"titulo": titulo, "fecha": fecha, "descripcion": descripcion}
        self.tareas.append(tarea)

        # Actualizar la lista de tareas en la interfaz
        self.lista_tareas.insert(tk.END, f"{fecha} - {titulo}")

        # Limpiar los campos
        self.titulo_entry.delete(0, tk.END)
        self.descripcion_text.delete("1.0", tk.END)

        messagebox.showinfo("Éxito", "Tarea agregada correctamente.")

    def ver_detalles(self):
        # Obtener la tarea seleccionada
        seleccion = self.lista_tareas.curselection()
        if not seleccion:
            messagebox.showerror("Error", "Por favor, selecciona una tarea.")
            return

        # Obtener los detalles de la tarea seleccionada
        indice = seleccion[0]
        tarea = self.tareas[indice]

        # Mostrar los detalles en un cuadro de mensaje
        detalles = f"Título: {tarea['titulo']}\nFecha: {tarea['fecha']}\nDescripción: {tarea['descripcion']}"
        messagebox.showinfo("Detalles de la Tarea", detalles)

if __name__ == "__main__":
    app = AgendaApp()
    app.mainloop()