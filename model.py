"""
    Este módulo es el encargado de conseguir la información requerida
    por el módulo 'controller'. Esto se logra a través de sus comunicaciones
    con la base de datos por medio de sus métodos.
"""
# Importación de librerias
from tkinter import *
from tkinter import messagebox as MessageBox
from PIL import ImageTk, Image
import tkinter as tk
import sqlite3
import re
from directorios import *
from conexion_base_datos import ConexionSql

mibase = sqlite3.connect("base_contactos.db")
micursor = mibase.cursor()


def para_agregar_contacto():
    """
    Este método crea un objeto de la clase Agenda y utiliza uno
    de sus métodos internos para crear un nuevo contacto.
    """
    agregar_contacto = Agenda()
    agregar_contacto.agregar_contacto()


def para_modificar_contacto():
    """
    Este método crea un objeto de la clase Agenda y utiliza uno
    de sus métodos internos para modificar un contacto existente.
    """
    mod_contacto = Agenda()
    mod_contacto.modificar_contacto()


def para_eliminar_contacto():
    """
    Este método crea un objeto de la clase Agenda y utiliza uno
    de sus métodos internos para eliminar un contacto existente.
    """
    elim_contacto = Agenda()
    elim_contacto.eliminar_contacto()


def para_ver_contactos():
    """
    Este método crea un objeto de la clase Agenda y utiliza uno
    de sus métodos internos para ver la lista de contactos existentes.
    """
    ver_contactos = Agenda()
    ver_contactos.ver_contactos()


class Agenda:
    """
    Esta clase contiene los métodos necesarios para el correcto
    funcionamiento de la aplicación, los cuales son llamados a
    través de los distintos botones.
    """

    def agregar_contacto(self):
        """
        Este método define la ventana a través de la cual se
        agregará el contacto y crea un diccionario dentro del cual
        se almacenan los datos del contacto creado, para luego ser
        mostrados al confirmar la creación.
        """

        def confirmar():
            """
            Este método tiene el propósito de verificar que se completen
            correctamente los datos y de agregar el diccionario del contacto
            creado a la lista 'contactos'. Así como también tiene el objetivo
            de ejecutar la consulta a SQL.
            """
            patron_nom = re.compile("^[A-zÑñ\s]+$").match(entry_nombre.get())
            patron_num = re.compile("^[0-9]+$").match(entry_numero.get())
            patron_ape = re.compile("^[A-zÑñ\s]+$").match(entry_apellido.get())

            if patron_nom and patron_num and patron_ape:
                contacto["nombre"] = entry_nombre.get()
                contacto["apellido"] = entry_apellido.get()
                contacto["numero"] = int(entry_numero.get())
                sql = "INSERT INTO contacto (nombre, apellido, numero) VALUES(?, ?, ?)"
                datos = (
                    entry_nombre.get(),
                    entry_apellido.get(),
                    entry_numero.get(),
                )
                micursor.execute(sql, datos)
                mibase.commit()
                MessageBox.showinfo(
                    "Contacto creado",
                    "Nombre: {}; Apellido: {}; Número: {}".format(
                        contacto["nombre"], contacto["apellido"], contacto["numero"]
                    ),
                )
                root.destroy()
            else:
                MessageBox.showerror("Error", "Revise los campos")

        # Diccionario en el que se almacenará el contacto creado
        contacto = {"nombre": "", "apellido": "", "numero": ""}
        # Declaración de la ventana donde se ingresarán los datos
        root = Tk()
        root.title("Agregar contacto")
        root.iconbitmap(ruta2)
        root.resizable(0, 0)
        root.geometry("280x210")
        root.config(bg="DeepSkyBlue2")

        label_nombre = Label(root, text="Nombre:")
        label_nombre.pack(padx=5, pady=5)
        label_nombre.config(bg="DeepSkyBlue2")
        entry_nombre = Entry(root)
        entry_nombre.pack()

        label_apellido = Label(root, text="Apellido:")
        label_apellido.pack(padx=5, pady=5)
        label_apellido.config(bg="DeepSkyBlue2")
        entry_apellido = Entry(root)
        entry_apellido.pack()

        label_numero = Label(root, text="Número:")
        label_numero.pack(padx=5, pady=5)
        label_numero.config(bg="DeepSkyBlue2")
        entry_numero = Entry(root)
        entry_numero.pack()

        espacio = Label(root, text="")
        espacio.pack()
        espacio.config(bg="DeepSkyBlue2")

        boton_confirmar = Button(
            root,
            text="Confirmar contacto",
            command=confirmar,
        )
        boton_confirmar.pack()
        boton_confirmar.config(bg="silver")

        root.mainloop()

    def modificar_contacto(self):
        """
        Este método define la ventana que será utilizada
        para la modificación de un contacto.
        """

        def modificar():
            """
            Este método realiza una consulta a la base de datos
            (busca los ID en la tabla), pide al usuario que ingrese
            un ID y, si ese ID es válido, despliega una ventana en la
            que el usuario puede modificar el contacto correspondiente
            a ese ID.
            """

            def final():
                """
                Este método tiene el propósito de verificar que se completen
                correctamente los datos y de actualizar la base de datos
                utilizando la información ingresada por el usuario.
                """
                patron_nom = re.compile("^[A-zÑñ\s]+$").match(entry_nom.get())
                patron_num = re.compile("^[0-9]+$").match(entry_tel.get())
                patron_ape = re.compile("^[A-zÑñ\s]+$").match(entry_ape.get())
                if patron_nom and patron_num and patron_ape:
                    nombre_new = entry_nom.get()
                    apellido_new = entry_ape.get()
                    telefono_new = entry_tel.get()
                    sql = "UPDATE contacto SET nombre=?, apellido=?, numero=? WHERE contacto_id=?"
                    datos_new = (nombre_new, apellido_new, telefono_new, cont_id)
                    micursor.execute(sql, datos_new)
                    mibase.commit()
                    MessageBox.showinfo("Operación realizada", "Contacto modificado")
                    root.destroy()
                else:
                    MessageBox.showerror("Error", "Revise los campos")

            sql = "SELECT contacto_id FROM contacto"
            micursor.execute(sql)
            resultado = micursor.fetchall()
            # Convierto la lista de tuplas devuelta por fetchall() a una lista
            result = []
            for t in resultado:
                for x in t:
                    result.append(x)
            try:
                cont_id = int(entry_id.get())
                # Consulto si el ID ingresado esta en la lista
                if cont_id in result:
                    root = Tk()
                    root.title("Modificar Contacto")
                    root.iconbitmap(ruta2)
                    root.resizable(0, 0)
                    root.geometry("280x210")
                    root.config(bg="DeepSkyBlue2")

                    label_nom = Label(root, text="Nuevo Nombre:")
                    label_nom.pack(padx=5, pady=5)
                    label_nom.config(bg="DeepSkyBlue2")
                    entry_nom = Entry(root)
                    entry_nom.pack()

                    label_ape = Label(root, text="Nuevo Apellido:")
                    label_ape.pack(padx=5, pady=5)
                    label_ape.config(bg="DeepSkyBlue2")
                    entry_ape = Entry(root)
                    entry_ape.pack()

                    label_tel = Label(root, text="Nuevo Número:")
                    label_tel.pack(padx=5, pady=5)
                    label_tel.config(bg="DeepSkyBlue2")
                    entry_tel = Entry(root)
                    entry_tel.pack()

                    espacio = Label(root, text="")
                    espacio.pack()
                    espacio.config(bg="DeepSkyBlue2")

                    boton_confirmar = Button(root, text="Confirmar", command=final)
                    boton_confirmar.pack()
                    boton_confirmar.config(bg="silver")

                    root.mainloop()
                else:
                    MessageBox.showerror(
                        "Error", "El contacto no se encuentra en la agenda"
                    )
            except ValueError:
                MessageBox.showerror("Error", "Debe ingresar un número")

        root = Tk()
        root.title("Ingresar ID")
        root.iconbitmap(ruta2)
        root.resizable(0, 0)
        root.geometry("280x110")
        root.config(bg="DeepSkyBlue2")

        label_id = Label(root, text="Contacto ID:")
        label_id.pack(padx=5, pady=5)
        label_id.config(bg="DeepSkyBlue2")
        entry_id = Entry(root)
        entry_id.pack()

        espacio = Label(root, text="")
        espacio.pack()
        espacio.config(bg="DeepSkyBlue2")

        boton_consultar = Button(root, text="Consultar", command=modificar)
        boton_consultar.pack()
        boton_consultar.config(bg="silver")

    def eliminar_contacto(self):
        """
        Este método define la ventana en la que podrá
        eliminarse un contacto a través de su ID.
        """

        def eliminar():
            """
            Este método tiene el propósito de verificar que se complete
            correctamente el campo ID, realizar una consulta a la base
            de datos para buscar todos los ID y luego eliminar el contacto
            correspondiente al ID ingresado por el usuario.
            """
            patron_num = re.compile("^[0-9]+$").match(entry_remove.get())
            sql = "SELECT contacto_id FROM contacto"
            micursor.execute(sql)
            resultado = micursor.fetchall()
            # Convierto la lista de tuplas devuelta por fetchall() a lista
            result = []
            for t in resultado:
                for x in t:
                    result.append(x)
            try:
                cont_id = int(entry_remove.get())
                # Consulto si el ID ingresado esta en la lista
                if cont_id in result and patron_num:
                    sql = "DELETE FROM contacto WHERE contacto_id=?"
                    rem = (cont_id,)
                    micursor.execute(sql, rem)
                    mibase.commit()
                    MessageBox.showinfo("Operación realizada", "Contacto eliminado")
                    root.destroy()
                else:
                    MessageBox.showerror(
                        "Error", "El contacto no se encuentra en la agenda"
                    )
            except ValueError:
                MessageBox.showerror("Error", "Debe ingresar un número")

        root = Tk()
        root.title("Eliminar Contacto")
        root.iconbitmap(ruta2)
        root.resizable(0, 0)
        root.geometry("270x107")
        root.config(bg="DeepSkyBlue2")
        label_remove = Label(root, text="Contacto ID:")
        label_remove.pack(padx=5, pady=5)
        label_remove.config(bg="DeepSkyBlue2")
        entry_remove = Entry(root)
        entry_remove.pack()

        espacio = Label(root, text="")
        espacio.pack()
        espacio.config(bg="DeepSkyBlue2")

        boton_confirmar = Button(root, text="Eliminar", command=eliminar)
        boton_confirmar.pack()
        boton_confirmar.config(bg="silver")

    def ver_contactos(self):
        """
        Este método, a través de una consulta a SQL,
        despliega una lista de los contactos creados.
        """
        sql = "SELECT * FROM contacto"
        micursor.execute(sql)
        resultado = micursor.fetchall()
        if len(resultado) > 0:
            root = Tk()
            root.title("Lista de contactos")
            root.config(bg="deep sky blue")
            for x in resultado:
                etiqueta = Label(
                    root,
                    text="              {}  -  {}  -  {}  -  {}             ".format(
                        x[0], x[1], x[2], x[3]
                    ),
                )
                etiqueta.pack()
                etiqueta.config(bg="deep sky blue")
                root.mainloop()
        else:
            MessageBox.showerror("Error", "Lista de contactos vacía")


info_class_agenda = Agenda()
print(info_class_agenda.__doc__)
