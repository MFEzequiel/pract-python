try:
  from tkinter import Frame
  from core import config
except ImportError as e:
  print('Error al importar la libreria -->', e)


class GUI(Frame):
  def __init__(self, root):
    super().__init__(root)
