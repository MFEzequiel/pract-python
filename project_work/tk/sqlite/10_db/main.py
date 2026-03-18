try:
  import os
  import sqlite3 as sql
  from tkinter import Tk
  from viewers import menu
except ImportError as e:
  print('Error al importar el módulo -->', e)

class FileManager:
  def __init__(self):
    pass

class Root:
  def __init__(self):
    self.root = Tk()
    self.root.title('MVC SQLite Manager - Demo')
    self.root.geometry('800x500+120+20')
    
    self.menu = menu.Menu(self.root)
    # main_viwer.MainViwer(self.root)

  def run(self):
    self.root.mainloop()

root = Root()
root.run()