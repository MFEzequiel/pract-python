# -*- coding: utf-8 -*-
try:
  from tkinter import Tk, Toplevel
  from ui import ui, menu, windows
  from command import game_logic
except ImportError:
  print('Error al importar las librerias')



class Root():
  def __init__(self) -> None:
    self.root = Tk()

    # config root
    self.root.title('Adivina el número')
    self.root.minsize('350', '350')
    
    # low and high number 
    # self.root_data = windows.WindowExtra(self.root)
    self.data = game_logic.GameLogic(1, 2, 3)
    self.data1 = self.data.input_data(2,3)
    print(self.data1["low"])
    # GUI
    self.menu = menu.GNUMenu(self.root)
    self.ui = ui.UI(self.root)
    

  def run(self):
    self.root.mainloop()

root = Root()
root.run()