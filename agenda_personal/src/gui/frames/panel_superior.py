import tkinter as tk
from tkinter import ttk

class PanelSuperior:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent, style="Panel.TFrame")
        self.crear_widgets()

    def crear_widgets(self):
        # Título
        ttk.Label(self.frame,
                 text="Agenda Personal",
                 style="Title.TLabel").pack(side=tk.LEFT, padx=10)

        # Estadísticas
        self.frame_stats = ttk.Frame(self.frame)
        self.frame_stats.pack(side=tk.RIGHT, padx=10)

        self.contador_eventos = ttk.Label(self.frame_stats,
                                        text="Total eventos: 0",
                                        style="Header.TLabel")
        self.contador_eventos.pack(side=tk.RIGHT)

    def actualizar_contador(self, total):
        self.contador_eventos.config(text=f"Total eventos: {total}")