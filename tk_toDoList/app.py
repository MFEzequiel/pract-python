try:
  from tkinter import Tk, Menu, ttk
  from ui import ui, menu
except ImportError:
  print("No se encontro la libreria, tkinter o ui", ImportError)

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

  def run(self):
    self.root.mainloop()

root = Root()
root.run()