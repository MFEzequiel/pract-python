# -*- coding: utf-8 -*-
try:
  from tkinter import Tk
  from core import config
  from ui import main_window, main_menu
except ImportError as e:
  print('Error al importar la libreria -->', e)

class Root:
  def __init__(self) -> None:
    self.root = Tk()
    self.root.title(config.title_app)
    self.root.geometry(config.size_app)

    # GUI
    main_menu.MainMenu(self.root)
    main_window.GUI(self.root)
  
  def run(self):
    self.root.mainloop()

root = Root()
root.run()