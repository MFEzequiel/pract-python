try:
  from tkinter import Frame, Menu
  from ui.db_viewa import ViewDataBase
except ImportError as e:
  print('Error al importar la librerias -->', e)

class UIMenu(Frame):
  def __init__(self, root) -> None:
    super().__init__(root)
    self.bar_menu = Menu(root)
    self.root = root.config(menu=self.bar_menu)

    # add options views table db
    self.option_sql = Menu(self.bar_menu)
    self.option_sql.add_command(label='Navegador SQL', command=lambda: ViewDataBase(root))

    # add cascade to menu
    self.bar_menu.add_cascade(label='Base de datos', menu=self.option_sql) 