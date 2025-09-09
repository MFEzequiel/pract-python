# -*- coding: utf-8 -*-
try:
  from tkinter import Tk
  from ui import main_window, menu
  from core import menu_act
except ImportError as e:
  print("No se encontro la librerias ", e)

class Root():
  def __init__(self) -> None:
    self.root = Tk()
    # configure root
    self.root.title('To Do List')
    self.root.resizable(0,0)
    self.root.minsize('350', '350')
    # self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    # call class ui
    self.menu = menu.UIMenu(self.root)
    self.ui = main_window.UI(self.root)

  def on_close(self):
    self.exit = menu_act.FuncionalityMenu()
    self.exit.destroy(file_save=False, root=self.root)

  def run(self):
    self.root.mainloop()

root = Root()
root.run()