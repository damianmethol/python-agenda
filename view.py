"""
Este módulo es el encargado de la parte visual de la aplicación.
"""
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from directorios import *
from model import Agenda
from model import para_agregar_contacto
from model import para_modificar_contacto
from model import para_eliminar_contacto
from model import para_ver_contactos


class VistaApp:
    """
    Esta clase es la encargada de crear la ventana principal
    de la interfaz gráfica perteneciente a la aplicación.
    """

    def __init__(self, window):
        self.root = window
        self.root.title("Agenda")
        self.root.geometry("250x410")
        self.root.resizable(0, 0)
        self.root.config(bg="deep sky blue")

        self.root.iconbitmap(ruta1)
        imagenruta = Image.open(ruta3)
        imagen = ImageTk.PhotoImage(imagenruta)
        label_imagen = Label(self.root, image=imagen)
        label_imagen.pack(padx=5, pady=13)
        label_imagen.config(bg="deep sky blue")

        # Creación de botones y organización de diseño
        boton_agregar = Button(
            self.root, text="Agregar contacto", command=para_agregar_contacto
        )
        boton_agregar.pack()
        boton_agregar.config(bg="silver")

        linea_espacio1 = Label(self.root, text="", height=1)
        linea_espacio1.pack()
        linea_espacio1.config(bg="deep sky blue")

        boton_modificar = Button(
            self.root,
            text="Modificar contacto",
            command=para_modificar_contacto,
        )
        boton_modificar.pack()
        boton_modificar.config(bg="silver")

        linea_espacio2 = Label(self.root, text="")
        linea_espacio2.pack()
        linea_espacio2.config(bg="deep sky blue")

        boton_eliminar = Button(
            self.root, text="Eliminar contacto", command=para_eliminar_contacto
        )
        boton_eliminar.pack()
        boton_eliminar.config(bg="silver")

        linea_espacio3 = Label(self.root, text="")
        linea_espacio3.pack()
        linea_espacio3.config(bg="deep sky blue")

        boton_ver = Button(self.root, text="Ver contactos", command=para_ver_contactos)
        boton_ver.pack()
        boton_ver.config(bg="silver")

        # Bucle de ejecución de la aplicación
        self.root.mainloop()
