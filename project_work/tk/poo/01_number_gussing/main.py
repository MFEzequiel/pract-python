# -*- coding: utf-8 -*-
try:
  from tkinter import Tk, Toplevel
  from ui import main_window, menu, two_windows
except ImportError as e:
  print('Error al importar las libreria -->', e)


class Root():
  def __init__(self) -> None:
    self.root = Tk()
    # config root
    self.root.title('Adivina el número')
    self.root.minsize('350', '350')
    # low and high number 
    self.root_data = two_windows.WindowExtra(self.root)
    # GUI
    self.menu = menu.GNUMenu(self.root)
    self.ui = main_window.UI(self.root)

  def run(self):
    self.root.mainloop()

root = Root()
root.run()