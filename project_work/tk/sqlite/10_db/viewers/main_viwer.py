try:
  from tkinter import Frame, Menu
except ImportError as e:
  print('Error al importar el módulo -->', e)

class MainViwer(Frame):
  def __init__(self, root=None):
    self.root = root
    # self._create_widgets()
    # Menu(self.root)

  def _create_widgets(self):
    # menubar = 
    pass