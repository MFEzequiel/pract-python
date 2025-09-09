try:
  from tkinter import Frame, Menu
  from core import menu_act
except ImportError as e:
  print('Error al importar la lbreria ', e)

class MainMenu(Frame):
  def __init__(self, root=None):
    # Create menu
    super().__init__(root)
    self.bar_menu = Menu(root)
    root.config(menu=self.bar_menu)

    # add options to menu file
    self.file = Menu(self.bar_menu)
    self.file.add_command(label='Nuevo')
    self.file.add_command(label='exportar Exel')
    self.file.add_command(label='salir', command=lambda: menu_act.FuncionalityMenu().destroy(root))
    # Add options to menu browser SQLite
    self.browser_sqlite = Menu(self.bar_menu)
    self.browser_sqlite.add_command(label='ver tablas')
    self.browser_sqlite.add_command(label='crear tablas')
    self.browser_sqlite.add_command(label='eliminar tablas')
    # Add options to menu register

    # Add option help

    # add cascade menu
    self.bar_menu.add_cascade(label='Archivo', menu=self.file)
    self.bar_menu.add_cascade(label='base de datos', menu=self.browser_sqlite)