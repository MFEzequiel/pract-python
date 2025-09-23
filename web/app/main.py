try:
  from tkinter import Tk
  from ui import main_window, menu
  from db import manager
except ImportError as e:
  print("Error al importar módulos. Asegúrate de tener instaladas las librerías necesarias: ", e)


class Root:
  def __init__(self) -> None:
    self.root = Tk()
    self.root.title("SQLite")
    self.root.geometry("400x200")
    self.root.resizable(0, 0)

    self.export_function = manager.ManagerDB.create_table
    # GUI
    menu.MenuApp(self.root, self.export_function)
    main_window.Main_Window(self.root)

  def run(self):
    self.root.mainloop()

if __name__ == '__main__':
  root = Root()
  root.run()