try:
  from tkinter import Tk  
  from core import config
  from ui import menu
  from database import manager
except ImportError as e:
  print('Erro al importar la libreria -->', e)

class Root:
  def __init__(self) -> None:
    self.root = Tk()
    self.root.title('Automatización SQLite')
    self.root.geometry("800x600")
    self.menu = menu.UIMenu(self.root)

    manager.ManagerDB().create_table_from_excel(config.path_directory_file_db, config.directory_files_excel)

    self.root.mainloop()

if __name__ == '__main__':
  app = Root()