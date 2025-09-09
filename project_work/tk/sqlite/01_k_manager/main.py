try:
  from tkinter import Tk
  from ui import main_window, main_menu
except ImportError as e:
  print('Error al impportar la libreria ', e)


class Root:
  def __init__(self) -> None:
    self.root = Tk()
    self.root.title('Administrador del kisko')
    self.root.geometry('350x400')

    #GUI
    self.menu = main_menu.MainMenu(self.root)
    self.ui = main_window.UI()

  def run(self):
    self.root.mainloop()

root = Root().run()