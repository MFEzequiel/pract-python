import tkinter as tk
from tkinter import ttk
from tkinter import Menu

# Funciones
def funcion_clik():

    _label.configure(text='' + name.get())
    _altura.configure(text='' + altura.get())




def _genero_():
    sel=genero.get()
    print(sel)

    if sel == 1:
        sex.configure(text='Hombre')
    elif sel == 2:
        sex.configure(text='Mujer')
    else:
        _label.configure(text='Error')


root = tk.Tk()

root.resizable(20,20)

# Barra de Menu
bmenu = Menu(root)
root.config(menu=bmenu)

# Agregar opciones al menú
op_menu = Menu(bmenu)
op_menu.add_command(label="Nuevo")
op_menu.add_separator()
op_menu.add_command(label="Salir")
bmenu.add_cascade(label='Archivo', menu=op_menu)

# Etiquetas
_label = ttk.Label(root, text='Nombre')
_label.grid(column=0, row=2)

sex = ttk.Label(root, text='Genero')
sex.grid(column=0, row=4)


_altura = ttk.Label(root, text='Altura')
_altura.grid(column=0, row=6)

# Caja de texto
name = tk.StringVar()
p_name = ttk.Entry(root, width=20, textvariable=name)
p_name.grid(column=0, row=1)

# variables
h = "Hombre"
m = "Mujer"

genero = tk.IntVar()
p_genero = ttk.Radiobutton(root, text=h, variable=genero, value=1, command=_genero_)
p_genero.grid(column=0, row=3, sticky=tk.W)

p_genero1 = ttk.Radiobutton(root, text=m, variable=genero, value=2, command=_genero_)
p_genero1.grid(column=1, row=3, sticky=tk.W)

altura = tk.StringVar()
p_altura = ttk.Entry(root, width=20, textvariable=altura)
p_altura.grid(column=0, row=5)

# Botones
bt_n = ttk.Button(root, text="Enviar", command=funcion_clik)

# Pociciones de los botones
bt_n.grid(column=0, row=7)

root.mainloop()