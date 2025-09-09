try:
  from tkinter import Frame, Menu
  from core import menu_act
  from ui.db_viewer import  ViewDataBase
except ImportError as e:
  print('Error al importar la librerias ', e)


class UIMenu(Frame):
  def __init__(self, root=None):
    super().__init__(root)

    # Create menu
    self.bar_menu = Menu(root)
    self.menu_func = menu_act.FuncionalityMenu()
    self.root = root.config(menu=self.bar_menu)

    # add options to menu file
    self.options_menu_00 = Menu(self.bar_menu)
    self.options_menu_00.add_command(label='Nuevo')
    self.options_menu_00.add_command(label='Exportar Excel', command=self.menu_func.export_data_excel)
    self.options_menu_00.add_command(label='Exportar PDF', command=self.menu_func.export_data_pdf)
    self.options_menu_00.add_command(label='Importar Excel', command=self.menu_func.import_data_excel)
    self.options_menu_00.add_command(label='Salir', command=lambda: self.menu_func.destroy(root))

    # Add options to menu register
    self.options_menu_01 = Menu(self.bar_menu)
    self.options_menu_01.add_cascade(label="Navegador SQLite", command=lambda: ViewDataBase(root))
    self.options_menu_01.add_cascade(label="crear")
    self.options_menu_01.add_cascade(label="eliminar")
    
    # Add option help
    self.options_menu_02 = Menu(self.bar_menu)
    self.options_menu_02.add_cascade(label="Acerca de")

    # add cascade menu
    self.bar_menu.add_cascade(label='Archivo', menu=self.options_menu_00)
    self.bar_menu.add_cascade(label='Base de datos', menu=self.options_menu_01)
    self.bar_menu.add_cascade(label='Ayuda', menu=self.options_menu_02)