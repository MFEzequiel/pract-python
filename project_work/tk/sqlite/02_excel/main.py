# -*- coding: utf-8 -*-
try:
  from tkinter import Tk
  from core import config
  from ui import main_window
except ImportError as e:
  print('Error al importar la libreria -->', e)

class Root:
  def __init__(self) -> None:
    self.root = Tk()

    # GUI
    main_window.GUI()
  
  def run(self):
    self.root.mainloop()

root = Root().run()