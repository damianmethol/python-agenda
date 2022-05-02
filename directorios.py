"""
Este módulo se encarga de importar las imágenes a la aplicación.
"""
import os

BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, "img")
ruta1 = STATIC_ROOT + "\\agregar.ico"
ruta2 = STATIC_ROOT + "\\contactos.ico"
ruta3 = STATIC_ROOT + "\\imagen.png"
