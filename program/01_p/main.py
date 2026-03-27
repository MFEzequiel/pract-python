try:
  import os
  import config
  from tkinter import Tk
  from views import main_window, menu
  from controllers import menu_act, manager_db
  from models import manager, model
except ImportError as e:
  print('Error al importar la librerias -->', e)

class Root:
  def __init__(self) -> None:
    self.root = Tk()
    self.root.title('Gestor Productos')
    self.root.geometry('500x450')

    # Crear directorio, base de datos y la tabla por defecto
    self.config = config.create_directory()

    self.db = manager.DBManager()
    self.conn = self.db.get_connect['conn']
    self.cr = self.db.get_connect['cursor']

    self.model = model.Model(self.conn, self.cr)
    self.model.defaul_create_table()

    self.ctrl_db = manager_db.CtrlDb(self.model)

    self.menu = menu.UIMenu(self.root, None, self.conn, self.cr, funcionality_menu=menu_act)
    self.ui = main_window.MainGUI(self.root, self.ctrl_db)

  def run(self) -> None:
    self.root.mainloop()


if __name__ == '__main__':
  root = Root()
  root.run()