from tkinter import *
from tkinter import messagebox, Menu

from bbdd import *
from borrar import *

root = Tk()
root.title('CRUD')
root.geometry('260x350')

#Creamos el menu de nuestra aplicación
menu = Menu(root)

#Cramos los submenus
#Submenu BBDD
menu_bbdd = Menu(menu, tearoff=0)
menu_bbdd.add_command(label='Conectar', command=conectar)
menu_bbdd.add_separator()
menu_bbdd.add_command(label='Salir', command=lambda: salir(root))
menu.add_cascade(label='BBDD', menu=menu_bbdd)
#Submenu Borrar
menu_borrar = Menu(menu, tearoff=0)
menu_borrar.add_command(label='Borrar campos', command=lambda: borra_campos(id_texto, nombre_texto, apellido_texto, 
direc_texto, pass_texto, coments))
menu.add_cascade(label='Borrar', menu=menu_borrar)
#Submenu CRUD
menu_crud = Menu(menu, tearoff=0)
menu_crud.add_command(label='Crear', command=lambda: insertar(name, apell, direc, passw, coments))
menu_crud.add_command(label='Leer', command=lambda: read(id_user, name, apell, direc, passw, coments))
menu_crud.add_command(label='Actualizar', command=lambda: actualizar(id_user, name, apell, direc, passw, coments))
menu_crud.add_command(label='Eliminar', command=lambda: eliminar(id_user))
menu.add_cascade(label='CRUD', menu=menu_crud)
#Submenu Ayuda
menu_help = Menu(menu, tearoff=0)
menu_help.add_command(label='Licencia')
menu_help.add_command(label='Acerca de')
menu.add_cascade(label='Ayuda', menu=menu_help)

#Mostramos el menu en nuestra app y los submenus
root.config(menu=menu)

#Campos de nuestra aplicación
#Etiquetas
id_label = Label(root, text='Id:')
id_label.grid(row=1, column=0, sticky='w', padx=10, pady=10, columnspan=4)
nombre_label = Label(root, text='Nombre:')
nombre_label.grid(row=2, column=0, sticky='w', padx=10, pady=10, columnspan=4)
apellido_label = Label(root, text='Apellido:')
apellido_label.grid(row=3, column=0, sticky='w', padx=10, pady=10, columnspan=4)
direc_label = Label(root, text='Dirección:')
direc_label.grid(row=4, column=0, sticky='w', padx=10, pady=10, columnspan=4)
pass_label = Label(root, text='Contraseña:')
pass_label.grid(row=5, column=0, sticky='w', padx=10, pady=10, columnspan=4)
coment_label = Label(root, text='Comentarios:')
coment_label.grid(row=6, column=0, sticky='w', padx=10, pady=10, columnspan=4)

id_user = StringVar()
name = StringVar()
apell = StringVar()
direc = StringVar()
passw = StringVar()

#Campos de texto
id_texto = Entry(root, width=25, textvariable=id_user)
id_texto.grid(row=1, column=1, columnspan=4)
nombre_texto = Entry(root, width=25, textvariable=name)
nombre_texto.grid(row=2, column=1, columnspan=4)
apellido_texto = Entry(root, width=25, textvariable=apell)
apellido_texto.grid(row=3, column=1, columnspan=4)
direc_texto = Entry(root, width=25, textvariable=direc)
direc_texto.grid(row=4, column=1, columnspan=4)
pass_texto = Entry(root, width=25, show='*', textvariable=passw)
pass_texto.grid(row=5, column=1, columnspan=4)
coments = Text(root, width=18, height=5)
coments.grid(row=6, column=1, padx=10, pady=10, columnspan=4)

#Creamos los botones de nuestro CRUD
create_btn = Button(root, text='Create', width=5, command=lambda: insertar(name, apell, direc, passw, coments))
create_btn.grid(row=7, column=0, padx=10, pady=10)
read_btn = Button(root, text='Read', width=5, command=lambda: read(id_user, name, apell, direc, passw, coments))
read_btn.grid(row=7, column=1, padx=10, pady=10)
update_btn = Button(root, text='Update', width=5, command=lambda: actualizar(id_user, name, apell, direc, passw, coments))
update_btn.grid(row=7, column=2, padx=10, pady=10)
delete_btn = Button(root, text='Delete', width=5, command=lambda: eliminar(id_user))
delete_btn.grid(row=7, column=3, padx=10, pady=10)

root.mainloop()