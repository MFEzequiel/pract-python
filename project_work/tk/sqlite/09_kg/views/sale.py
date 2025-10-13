try:
  from tkinter import Frame, Label, StringVar, Entry, Button
except ImportError as e:
  print('Error al importar el módulo -->', e)

class Sale(Frame):
  def __init__(self, root=None) -> None:
    pass