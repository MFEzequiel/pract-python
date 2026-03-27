# -*- coding: utf-8 -*-
try:
  import os
  from tkinter import Tk
  from ui import main_window
except ImportError as e:
  print('Erro al importar la libreria -->', e)

class Root:
  def __init__(self):
    self.root = Tk()
    self.root.title('Formulario')
    self.root.geometry('250x350')
    self.root.config(bg='#4B6587')
    
    # GUI
    main_window.GUI(self.root)

  def run(self):
    self.root.mainloop()

root = Root()
root.run()
