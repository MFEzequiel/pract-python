try:
  from tkinter import Tk
  import config
  from views import menu, gui_main, db_viewer
  from modules import manager_db, model_db
except ImportError as e:
  print('Error al importar el módulo -->', e)


class Root:
  def __init__(self) -> None:
    self.root = Tk()
    self.root.title('Mini Marker v1.0')
    self.root.geometry("1050x650+120+20")

    # Create directories
    config.create_directories()

    # connection to db and create data base default
    self.db = manager_db.DBManager(config.DIR_FILE_DB)
    conn = self.db.connect_db['conn']
    cursor = self.db.connect_db['cursor']

    # # create tabe for default
    model_db.DBModel(conn, cursor)

    # GUI
    menu.UIMenu(self.root, db_viewer.ViewDataBase)
    gui_main.GUI(self.root, conn, cursor)

  def run(self):
    self.root.mainloop()


root = Root()
root.run()