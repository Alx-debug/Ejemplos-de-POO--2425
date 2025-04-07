import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from task_manager import TaskManager
import json
from datetime import datetime

class TodoApp:
    def __init__(self, root):
        """
        Inicializa la aplicación
        Args:
            root: Ventana principal de Tkinter
        """
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("500x600")

        # Inicializar el gestor de tareas
        self.task_manager = TaskManager()

        # Variables de Tkinter
        self.var_nueva_tarea = tk.StringVar()
        self.var_filtro = tk.StringVar(value="todas")
        self.var_prioridad = tk.StringVar(value="normal")

        # Configurar la interfaz
        self.crear_interfaz()
        self.configurar_atajos()

        # Intentar cargar tareas guardadas
        self.cargar_tareas()

    def crear_interfaz(self):
        """Crea todos los elementos de la interfaz gráfica"""
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Frame superior para entrada y filtros
        top_frame = ttk.Frame(main_frame)
        top_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)

        # Campo de entrada
        self.entrada_tarea = ttk.Entry(
            top_frame,
            textvariable=self.var_nueva_tarea,
            width=30
        )
        self.entrada_tarea.grid(row=0, column=0, padx=5)

        # Selector de prioridad
        prioridades = ttk.Combobox(
            top_frame,
            textvariable=self.var_prioridad,
            values=["baja", "normal", "alta"],
            width=8
        )
        prioridades.grid(row=0, column=1, padx=5)
        prioridades.set("normal")

        # Botón añadir
        btn_agregar = ttk.Button(
            top_frame,
            text="Añadir",
            command=self.agregar_tarea
        )
        btn_agregar.grid(row=0, column=2, padx=5)

        # Frame de filtros
        filter_frame = ttk.Frame(main_frame)
        filter_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)

        # Botones de filtro
        ttk.Radiobutton(
            filter_frame,
            text="Todas",
            variable=self.var_filtro,
            value="todas",
            command=self.actualizar_lista
        ).pack(side=tk.LEFT, padx=5)

        ttk.Radiobutton(
            filter_frame,
            text="Pendientes",
            variable=self.var_filtro,
            value="pendientes",
            command=self.actualizar_lista
        ).pack(side=tk.LEFT, padx=5)

        ttk.Radiobutton(
            filter_frame,
            text="Completadas",
            variable=self.var_filtro,
            value="completadas",
            command=self.actualizar_lista
        ).pack(side=tk.LEFT, padx=5)

        # Lista de tareas
        self.lista_tareas = ttk.Treeview(
            main_frame,
            columns=("estado", "prioridad", "fecha"),
            show="headings",
            height=15
        )

        # Configurar columnas
        self.lista_tareas.heading("estado", text="Estado")
        self.lista_tareas.heading("prioridad", text="Prioridad")
        self.lista_tareas.heading("fecha", text="Fecha")

        self.lista_tareas.column("estado", width=100)
        self.lista_tareas.column("prioridad", width=100)
        self.lista_tareas.column("fecha", width=150)

        self.lista_tareas.grid(row=2, column=0, pady=10, sticky=(tk.W, tk.E))

        # Scrollbar para la lista
        scrollbar = ttk.Scrollbar(
            main_frame,
            orient=tk.VERTICAL,
            command=self.lista_tareas.yview
        )
        scrollbar.grid(row=2, column=1, sticky=(tk.N, tk.S))
        self.lista_tareas.configure(yscrollcommand=scrollbar.set)

        # Frame de botones
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, pady=5)

        # Botones de acción
        ttk.Button(
            button_frame,
            text="Completar (C)",
            command=self.completar_tarea
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            button_frame,
            text="Eliminar (D)",
            command=self.eliminar_tarea
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            button_frame,
            text="Limpiar Completadas",
            command=self.limpiar_completadas
        ).pack(side=tk.LEFT, padx=5)

        # Etiqueta de estadísticas
        self.label_stats = ttk.Label(main_frame, text="")
        self.label_stats.grid(row=4, column=0, pady=5)

        # Etiqueta de atajos
        ttk.Label(
            main_frame,
            text="Atajos: Enter = Añadir, C = Completar, D = Eliminar, Esc = Salir",
            wraplength=400
        ).grid(row=5, column=0, pady=5)

    def configurar_atajos(self):
        """Configura los atajos de teclado"""
        self.root.bind('<Return>', lambda e: self.agregar_tarea())
        self.root.bind('<c>', lambda e: self.completar_tarea())
        self.root.bind('<d>', lambda e: self.eliminar_tarea())
        self.root.bind('<Escape>', lambda e: self.salir_aplicacion())

    def agregar_tarea(self):
        """Agrega una nueva tarea a la lista"""
        texto = self.var_nueva_tarea.get().strip()
        if texto:
            if not self.task_manager.existe_tarea(texto):
                self.task_manager.agregar_tarea(texto)
                ultima_tarea = self.task_manager.obtener_tarea(self.task_manager.total_tareas() - 1)
                ultima_tarea.establecer_prioridad(self.var_prioridad.get())
                self.var_nueva_tarea.set("")
                self.actualizar_lista()
                self.guardar_tareas()
            else:
                messagebox.showwarning("Advertencia", "Esta tarea ya existe")
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese una tarea")

    def completar_tarea(self):
        """Marca la tarea seleccionada como completada"""
        seleccion = self.lista_tareas.selection()
        if seleccion:
            indice = self.lista_tareas.index(seleccion[0])
            self.task_manager.completar_tarea(indice)
            self.actualizar_lista()
            self.guardar_tareas()
        else:
            messagebox.showwarning("Advertencia", "Por favor seleccione una tarea")

    def eliminar_tarea(self):
        """Elimina la tarea seleccionada"""
        seleccion = self.lista_tareas.selection()
        if seleccion:
            indice = self.lista_tareas.index(seleccion[0])
            if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar esta tarea?"):
                self.task_manager.eliminar_tarea(indice)
                self.actualizar_lista()
                self.guardar_tareas()
        else:
            messagebox.showwarning("Advertencia", "Por favor seleccione una tarea")

    def limpiar_completadas(self):
        """Elimina todas las tareas completadas"""
        if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar todas las tareas completadas?"):
            tareas_eliminadas = self.task_manager.limpiar_completadas()
            self.actualizar_lista()
            self.guardar_tareas()
            messagebox.showinfo("Información", f"Se eliminaron {tareas_eliminadas} tareas completadas")

    def actualizar_lista(self):
        """Actualiza la lista de tareas en la interfaz"""
        # Limpiar lista actual
        for item in self.lista_tareas.get_children():
            self.lista_tareas.delete(item)

        # Filtrar tareas según selección
        filtro = self.var_filtro.get()
        for i, tarea in enumerate(self.task_manager.obtener_tareas()):
            if filtro == "todas" or \
               (filtro == "pendientes" and not tarea.completada) or \
               (filtro == "completadas" and tarea.completada):

                estado = "✓" if tarea.completada else "□"
                fecha = tarea.fecha_completado if tarea.completada else tarea.fecha_creacion
                fecha_str = fecha.strftime("%Y-%m-%d %H:%M")

                self.lista_tareas.insert(
                    "",
                    tk.END,
                    values=(estado, tarea.prioridad, fecha_str),
                    text=tarea.texto
                )

        # Actualizar estadísticas
        total = self.task_manager.total_tareas()
        completadas = self.task_manager.tareas_completadas()
        pendientes = self.task_manager.tareas_pendientes()
        self.label_stats.config(
            text=f"Total: {total} | Completadas: {completadas} | Pendientes: {pendientes}"
        )

    def guardar_tareas(self):
        """Guarda las tareas en un archivo JSON"""
        try:
            tareas = [tarea.to_dict() for tarea in self.task_manager.obtener_tareas()]
            with open('tareas.json', 'w') as f:
                json.dump(tareas, f)
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar las tareas: {str(e)}")

    def cargar_tareas(self):
        """Carga las tareas desde un archivo JSON"""
        try:
            with open('tareas.json', 'r') as f:
                tareas = json.load(f)
                for tarea_dict in tareas:
                    tarea = self.task_manager.Task.from_dict(tarea_dict)
                    self.task_manager.tareas.append(tarea)
            self.actualizar_lista()
        except FileNotFoundError:
            pass  # No hay archivo de tareas, comenzar con lista vacía
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar las tareas: {str(e)}")

    def salir_aplicacion(self):
        """Guarda las tareas y cierra la aplicación"""
        self.guardar_tareas()
        self.root.quit() 
