import sqlite3
from tkinter import *
from tkinter import messagebox

def conectar():
    conector = sqlite3.connect('database_crud')
    cursor = conector.cursor()
    try:
        cursor.execute('''CREATE TABLE datos_usuarios(
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(30),
            apellido VARCHAR(30),
            direccion VARCHAR(100),
            password VARCHAR(20),
            comentarios VARCHAR(110)
        )''')
        messagebox.showinfo('BBDD', 'La BBDD ha sido creada exitosamente.')
    except sqlite3.OperationalError:
        messagebox.showwarning('BBDD', 'La base de datos ya ha sido creada')
        #conector.close()

def insertar(t1,t2,t3,t4,t5):
    conector = sqlite3.connect('database_crud')
    cursor = conector.cursor()
    
    cursor.execute("INSERT INTO datos_usuarios VALUES (NULL, '" + t1.get() +
        "','" + t2.get() +
        "','" + t3.get() +
        "','" + t4.get() +
        "','" + t5.get('1.0', END) + "')")
    conector.commit()
    messagebox.showinfo('CRUD', 'Datos registrados exitosamente')

def read(t1,t2,t3,t4,t5,t6):
    conector = sqlite3.connect('database_crud')
    cursor = conector.cursor()

    cursor.execute("SELECT * FROM datos_usuarios WHERE id_usuario = '"+ t1.get() +"'")
    conector.commit()
    registros = cursor.fetchall()

    for registro in registros:
        t2.set(registro[1])
        t3.set(registro[2])
        t4.set(registro[3])
        t5.set(registro[4])
        t6.insert(INSERT, registro[5])

def eliminar(t1):
    conector = sqlite3.connect('database_crud')
    cursor = conector.cursor()

    cursor.execute("DELETE FROM datos_usuarios WHERE id_usuario = '" + t1.get() + "'")
    resp = messagebox.askquestion('Eliminar registro', '¿Estás seguro de eliminar este registro? Se eliminará de forma permanente')
    if resp == 'yes':
        conector.commit()
        messagebox.showinfo('Eliminar registro', 'Registro eliminado con éxito')

def actualizar(t1,t2,t3,t4,t5,t6):
    conector = sqlite3.connect('database_crud')
    cursor = conector.cursor()

    cursor.execute("UPDATE datos_usuarios SET nombre = '" + t2.get() + 
    "', apellido = '" + t3.get() +
    "', direccion = '" + t4.get() +
    "', password = '" + t5.get() +
    "', comentarios = '" + t6.get('1.0', END) +
    "' WHERE id_usuario = '" + t1.get() + "'")

    resp = messagebox.askquestion('Actualizar', '¿Estás seguro de que quieres actualizar el registro?\nNo se podrán rehacer los cambios')

    if resp == 'yes':
        conector.commit()
        messagebox.showinfo('Actualizar', 'Cambios realizados con éxito')


def salir(ventana):
    valor = messagebox.askquestion('Salir', '¿Deseas salir de la aplicación?')
    if valor=='yes':
        ventana.destroy()
