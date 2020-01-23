from tkinter import *
from tkinter import messagebox

def borra_campos(t1, t2, t3, t4, t5, t6):
    try:
        t1.delete(0, END)
        t2.delete(0, END)
        t3.delete(0, END)
        t4.delete(0, END)
        t5.delete(0, END)
        t6.delete('1.0', END)
    except:
        messagebox.showwarning('Borrar datos', 'Los campos están vacíos')