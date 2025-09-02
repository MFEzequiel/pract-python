# Importar librería
import tkinter as tk
from tkinter import ttk
import math

# Functions
def insertValue(n):
  if n >= '0' and n <= '9' or n == '(' or n == ')' or n == '.': 
    label_2.set(label_2.get() + n)

  if n == '*' or n == '+' or n == '-' or n == '/':
    if n == '*':
      label_1.set(label_2.get() + '*')
    elif n == '+':
      label_1.set(label_2.get() + '+')
    elif n == '-':
      label_1.set(label_2.get() + '-')
    elif n == '/':
      label_1.set(label_2.get() + '/')
    
    label_2.set('')
  
  if n == '=':
    label_1.set(label_1.get() + label_2.get())
    result = eval(label_1.get())
    label_2.set(result)


def raizCuadrada():
  label_1.set('')
  result = math.sqrt(float(label_2.get()))
  label_2.set(result)


def clear():
  inicio = 0
  finish = len(label_2.get())
  label_2.set(label_2.get()[inicio:finish-1])


def allDelete():
  label_1.set("")
  label_2.set("")


# Inicializar ventana
root = tk.Tk()
root.title('Python – Tkinter')
root.geometry('+500+80')

# Style
style = ttk.Style(root)
style.configure('mainframe.TFrame', background='#D8D8D8')

style = ttk.Style()
style.configure('label.TLabel', font='arial 15', anchor='E')

# style = ttk.Style()
# style.configure('label2.TLabel', font='arial 15', anchor='E')

# Elements

mainframe = ttk.Frame(root, style='mainframe.TFrame')

label_1 = tk.StringVar()
label_entry_1 = ttk.Label(mainframe, textvariable=label_1, style='label.TLabel')

label_2 = tk.StringVar()
label_entry_2 = ttk.Label(mainframe, textvariable=label_2, style='label2.TLabel')

bt_0 = ttk.Button(mainframe, text='0', command=lambda : insertValue('0'))
bt_1 = ttk.Button(mainframe, text='1', command=lambda : insertValue('1'))
bt_2 = ttk.Button(mainframe, text='2', command=lambda : insertValue('2'))
bt_3 = ttk.Button(mainframe, text='3', command=lambda : insertValue('3'))
bt_4 = ttk.Button(mainframe, text='4', command=lambda : insertValue('4'))
bt_5 = ttk.Button(mainframe, text='5', command=lambda : insertValue('5'))
bt_6 = ttk.Button(mainframe, text='6', command=lambda : insertValue('6'))
bt_7 = ttk.Button(mainframe, text='7', command=lambda : insertValue('7'))
bt_8 = ttk.Button(mainframe, text='8', command=lambda : insertValue('8'))
bt_9 = ttk.Button(mainframe, text='9', command=lambda : insertValue('9'))

bt_delete = ttk.Button(mainframe, text=chr(9003), command=lambda: clear())
bt_all_delete = ttk.Button(mainframe, text='C', command=lambda: allDelete())
bt_parent_1 = ttk.Button(mainframe, text='(', command=lambda: insertValue('('))
bt_parent_2 = ttk.Button(mainframe, text=')', command=lambda: insertValue(')'))
bt_pointer = ttk.Button(mainframe, text='.', command=lambda: insertValue('.'))

bt_div = ttk.Button(mainframe, text=chr(247), command=lambda: insertValue('/'))
bt_mul = ttk.Button(mainframe, text='*', command=lambda: insertValue('*'))
bt_sum = ttk.Button(mainframe, text='+', command=lambda: insertValue('+'))
bt_res = ttk.Button(mainframe, text='-', command=lambda: insertValue('-'))

bt_ecual = ttk.Button(mainframe, text='=', command=lambda: insertValue('='))
bt_raiz = ttk.Button(mainframe, text='✔️', command=lambda: raizCuadrada())

# Position elements
mainframe.grid(column=0, row=0)
label_entry_1.grid(column=0, row=0, columnspan=4, sticky=(tk.W, tk.E))
label_entry_2.grid(column=0, row=1, columnspan=4, sticky=(tk.W, tk.E))

bt_parent_1.grid(column=0, row=2)
bt_parent_2.grid(column=1, row=2)
bt_all_delete.grid(column=2, row=2)
bt_delete.grid(column=3, row=2)

bt_div.grid(column=3, row=3)
bt_9.grid(column=2, row=3)
bt_8.grid(column=1, row=3)
bt_7.grid(column=0, row=3)

bt_mul.grid(column=3, row=4)
bt_6.grid(column=2, row=4)
bt_5.grid(column=1, row=4)
bt_4.grid(column=0, row=4)

bt_sum.grid(column=3, row=5)
bt_3.grid(column=2, row=5)
bt_2.grid(column=1, row=5)
bt_1.grid(column=0, row=5)

bt_res.grid(column=3, row=6)
bt_pointer.grid(column=2, row=6)
bt_0.grid(column=0, row=6, columnspan=2, sticky=(tk.W, tk.E))

bt_raiz.grid(column=3, row=7)
bt_ecual.grid(column=0, row=7, columnspan=3, sticky=(tk.W, tk.E))

# Activar ventana
root.mainloop()