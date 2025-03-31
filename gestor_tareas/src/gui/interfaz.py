import tkinter as tk
from tkinter import ttk, messagebox
from src.logic.gestor_tareas import GestorTareas

class InterfazGestorTareas:
    """
    Clase que maneja la interfaz gráfica.
    """
    def __init__(self):
        self.gestor = GestorTareas()
        self.ventana = tk.Tk()
        self.ventana.title("Gestor de Tareas")
        self.ventana.geometry("500x600")

        self.configurar_ventana()
        self.crear_widgets()
        self.configurar_eventos()

        self.gestor.agregar_observador(self.actualizar_lista_tareas)

    def configurar_ventana(self):
        """Configura las propiedades básicas de la ventana."""
        self.ventana.configure(bg='#f0f0f0')
        self.ventana.grid_columnconfigure(0, weight=1)
        self.ventana.grid_rowconfigure(2, weight=1)

    def crear_widgets(self):
        """Crea y configura todos los widgets de la interfaz."""
        self.frame_entrada = ttk.Frame(self.ventana, padding="10")
        self.frame_entrada.grid(row=0, column=0, sticky="ew")

        self.entrada_tarea = ttk.Entry(
            self.frame_entrada,
            width=40,
            font=('Arial', 10)
        )
        self.entrada_tarea.pack(fill=tk.X, expand=True)

        self.frame_lista = ttk.Frame(self.ventana, padding="10")
        self.frame_lista.grid(row=1, column=0, sticky="nsew")

        self.lista_tareas = tk.Listbox(
            self.frame_lista,
            height=15,
            font=('Arial', 10),
            selectmode=tk.SINGLE
        )
        self.lista_tareas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(
            self.frame_lista,
            orient=tk.VERTICAL,
            command=self.lista_tareas.yview
        )
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.lista_tareas.configure(yscrollcommand=scrollbar.set)

        self.frame_botones = ttk.Frame(self.ventana, padding="10")
        self.frame_botones.grid(row=2, column=0, sticky="ew")

        self.btn_agregar = ttk.Button(
            self.frame_botones,
            text="Agregar Tarea",
            command=self.agregar_tarea
        )
        self.btn_agregar.pack(side=tk.LEFT, padx=5)

        self.btn_completar = ttk.Button(
            self.frame_botones,
            text="Marcar Completada",
            command=self.marcar_completada
        )
        self.btn_completar.pack(side=tk.LEFT, padx=5)

        self.btn_eliminar = ttk.Button(
            self.frame_botones,
            text="Eliminar Tarea",
            command=self.eliminar_tarea
        )
        self.btn_eliminar.pack(side=tk.LEFT, padx=5)

    def configurar_eventos(self):
        """Configura los manejadores de eventos."""
        self.entrada_tarea.bind('<Return>', lambda e: self.agregar_tarea())
        self.lista_tareas.bind('<Double-Button-1>', lambda e: self.marcar_completada())
        self.lista_tareas.bind('<Delete>', lambda e: self.eliminar_tarea())

    def agregar_tarea(self):
        """Maneja la lógica de agregar una nueva tarea."""
        texto = self.entrada_tarea.get().strip()
        if self.gestor.agregar_tarea(texto):
            self.entrada_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning(
                "Error",
                "Por favor ingrese una tarea válida."
            )

    def marcar_completada(self):
        """Maneja la lógica de marcar una tarea como completada."""
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            if self.gestor.marcar_completada(seleccion[0]):
                self.actualizar_lista_tareas()
        else:
            messagebox.showinfo(
                "Selección Requerida",
                "Por favor seleccione una tarea."
            )

    def eliminar_tarea(self):
        """Maneja la lógica de eliminar una tarea."""
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            if messagebox.askyesno("Confirmar", "¿Desea eliminar esta tarea?"):
                if self.gestor.eliminar_tarea(seleccion[0]):
                    self.actualizar_lista_tareas()
        else:
            messagebox.showinfo(
                "Selección Requerida",
                "Por favor seleccione una tarea."
            )

    def actualizar_lista_tareas(self):
        """Actualiza la visualización de la lista de tareas."""
        self.lista_tareas.delete(0, tk.END)
        for tarea in self.gestor.obtener_tareas():
            self.lista_tareas.insert(tk.END, str(tarea))

    def iniciar(self):
        """Inicia la aplicación."""
        self.ventana.mainloop()