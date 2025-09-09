try:
  from tkinter import Frame
except ImportError as e:
  print('Error al impportar la libreria ', e)

class UI(Frame):
  pass