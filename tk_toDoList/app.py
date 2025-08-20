# -*- coding: utf-8 -*-
try:
  from tkinter import Tk
  from ui import ui, menu
  from db import factoryDB
except ImportError:
  print("No se encontro la librerias", ImportError)

class Root():
  def __init__(self) -> None:
    self.root = Tk()
    # configure root
    self.root.title('To Do List')
    self.root.resizable(0,0)
    self.root.minsize('350', '350')

    # call class ui
    self.menu = menu.UIMenu(self.root)
    self.ui = ui.UI(self.root)

    # db
    self.name_db = 'example.db'
    self.folder = './db/folderDB'
    self.db = factoryDB.FactoryDB(self.name_db, self.folder)

  def run(self):
    self.root.mainloop()

root = Root()
root.run()