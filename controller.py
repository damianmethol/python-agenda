"""
Este módulo es el encargado de realizar el pedido
de ejecución de la aplicación y sus funcionalidades.
"""
from tkinter import Tk
from view import VistaApp
from model import Agenda
from conexion_base_datos import ConexionSql

conexion_sql = ConexionSql()
conexion_sql.conexion_base()


class MiApp:
    """
    Esta clase es la encargada de lanzar la ejecución de la aplicación.
    """

    def __init__(self, window):
        """
        Este método se encarga de lanzar la interfaz gráfica de la aplicación.
        """
        self.ventana = window
        VistaApp(self.ventana)


if __name__ == "__main__":
    root = Tk()
    obj = MiApp(root)
    root.mainloop()
