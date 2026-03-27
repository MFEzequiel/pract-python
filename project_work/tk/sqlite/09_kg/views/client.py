try:
  from tkinter import Frame, Label, StringVar, Entry, Button
except ImportError as e:
  print('Error al importar el módulo -->', e)

class Clients(Frame):
  def __init__(self, root=None) -> None:
    label = Label(root, text='Clientes')
    label.pack(padx=1)