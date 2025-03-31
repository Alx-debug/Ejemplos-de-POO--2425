from tkinter import ttk

def configurar_estilos():
    style = ttk.Style()

    # Estilos para frames
    style.configure("Panel.TFrame",
                   background="#f0f0f0",
                   relief="raised")

    # Estilos para etiquetas
    style.configure("Title.TLabel",
                   font=("Helvetica", 12, "bold"),
                   padding=10)
    style.configure("Header.TLabel",
                   font=("Helvetica", 11),
                   padding=5)

    # Estilos para botones
    style.configure("Action.TButton",
                   font=("Helvetica", 10),
                   padding=5)
    style.configure("Delete.TButton",
                   font=("Helvetica", 10),
                   padding=5,
                   background="red")