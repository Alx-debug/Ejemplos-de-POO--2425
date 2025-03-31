import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry  # Asegúrate de tener instalado tkcalendar

class AgendaApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Agenda Personal")
        self.geometry("800x600")

        # Crear los frames para organizar la interfaz
        self.create_widgets()

    def create_widgets(self):
        # Frame superior para la entrada de datos
        self.input_frame = tk.Frame(self, padx=10, pady=10)
        self.input_frame.pack(fill=tk.X)

        # Etiqueta y campo de entrada para el título del evento
        tk.Label(self.input_frame, text="Título:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.title_entry = tk.Entry(self.input_frame, width=40)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y selector de fecha
        tk.Label(self.input_frame, text="Fecha:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.date_entry = DateEntry(self.input_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.grid(row=1, column=1, padx=5, pady=5)

        # Botón para agregar eventos
        self.add_button = tk.Button(self.input_frame, text="Agregar Evento", command=self.add_event)
        self.add_button.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)

        # Frame inferior para la lista de eventos
        self.list_frame = tk.Frame(self, padx=10, pady=10)
        self.list_frame.pack(fill=tk.BOTH, expand=True)

        # Treeview para mostrar los eventos
        self.event_tree = ttk.Treeview(self.list_frame, columns=("Fecha", "Título"), show="headings")
        self.event_tree.heading("Fecha", text="Fecha")
        self.event_tree.heading("Título", text="Título")
        self.event_tree.pack(fill=tk.BOTH, expand=True)

    def add_event(self):
        # Obtener los datos de entrada
        title = self.title_entry.get()
        date = self.date_entry.get()

        # Validar que el título no esté vacío
        if not title:
            tk.messagebox.showerror("Error", "El título no puede estar vacío.")
            return

        # Agregar el evento al Treeview
        self.event_tree.insert("", "end", values=(date, title))

        # Limpiar los campos de entrada
        self.title_entry.delete(0, tk.END)
        self.date_entry.set_date("")

if __name__ == "__main__":
    app = AgendaApp()
    app.mainloop()