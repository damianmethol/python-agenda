"""
Este módulo es el encargado de realizar la conexión 
con la base de datos o de crearla si no existe.
"""
import sqlite3


class ConexionSql:
    """
    Esta clase se encarga de realizar la conexión con la
    base de datos SQL o de crearla en caso de que no exista.
    """

    def conexion_base(self):
        """
        Este método se encarga de realizar la conexión con la
        base de datos SQL o de crearla en caso de que no exista.
        """
        mibase = sqlite3.connect("base_contactos.db")
        micursor = mibase.cursor()
        micursor.execute(
            "CREATE TABLE IF NOT EXISTS contacto (contacto_id integer NOT NULL PRIMARY KEY AUTOINCREMENT, nombre varchar(20) NOT NULL, apellido varchar(20) NOT NULL, numero UNSIGNED BIGINT(10) NOT NULL)"
        )
        print("Conexión con la base de datos establecida")
