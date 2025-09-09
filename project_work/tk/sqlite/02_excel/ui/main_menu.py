try:
  from tkinter import Frame, Menu
  from core import config
except ImportError as e:
  print('Error al importar la libreria -->', e)

class MainMenu(Frame):
  def __init__(self, root):
    pass