import tkinter as tk
from tkinter import ttk

# functions
def Distance():
  result = float(metros_segundo.get()) * float(metros_tiempo.get())
  print(result)
  label.configure(text=f'Distancia recorida {result} metros')

# Initialice root
root = tk.Tk()
root.title('Distancia recorrida por un auto')
root.geometry('+500+80')

# Crete element
label = ttk.Label(root, text='Distancia recorida por un auto')
label_metros_segundo = ttk.Label(root, text='Metros por segundo')
label_tiempo = ttk.Label(root, text='Tiempo en minutos')

# Distacia recorrida
metros_segundo = tk.StringVar()
metros_tiempo = tk.StringVar()

entrada_metro_segundo = ttk.Entry(root, width=20, textvariable=metros_segundo)
entrada_metro_tiempo = ttk.Entry(root, width=20, textvariable=metros_tiempo)

bt = ttk.Button(root, text='result', command=lambda : Distance())

# Position element
label.grid(column=0, row=0)
label_metros_segundo.grid(column=0, row=1)
label_tiempo.grid(column=0, row=2)

entrada_metro_segundo.grid(column=1, row=1)
entrada_metro_tiempo.grid(column=1, row=2)

bt.grid(column=0, row=4)

root.mainloop()