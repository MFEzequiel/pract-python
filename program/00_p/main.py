try:
  import os
  from core import config
  from tkinter import Tk
  from ui import main_window, menu
  from db.manager import DBManager
except ImportError as e:
  print('Error al importar la librerias -->', e)

class Root:
  def __init__(self) -> None:
    self.root = Tk()
    self.root.title('Gestor Productos')
    self.root.geometry('500x450')

    self.db = DBManager()

    self.menu = menu.UIMenu(self.root)
    self. ui = main_window.MainGUI(self.root)

  def run(self):
    self.root.mainloop()


if __name__ == '__main__':
  root = Root()
  root.run()