# -*- coding: utf-8 -*-
try:
  from tkinter import Tk
  import os
  from core import config
  from ui import menu
except ImportError as e:
  print('Erro al importar el modulo -->', e)

class Root:
  def __init__(self) -> None:
    self.root = Tk()
    self.root.title('SQLite')
    self.root.geometry("800x500")

    if not os.path.exists(config.custom_full_db_path):
      os.makedirs(config.custom_full_db_path)

    # GUI
    menu.Menu(self.root)

    
  def run(self):
    self.root.mainloop()

root = Root()
root.run()