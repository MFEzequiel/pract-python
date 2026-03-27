# -*- coding: utf-8 -*-
try:
  from tkinter import Tk
  from views.interface import Interfaz
  from controllers import ctrl_cart
except ImportError as e:
  print('Error al importar el modulo -->', e)

class Root:
  def __init__(self):
    self.root = Tk()

    self.ui = Interfaz(self.root)
    self.controller = ctrl_cart.Controlador(self.ui)
    self.ui.controlador = self.controller  # asignación circular

  def run(self):
    self.root.mainloop()

if __name__ == "__main__":
  root = Root()
  root.run()