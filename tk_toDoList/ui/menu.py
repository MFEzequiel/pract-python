try:
  from tkinter import Frame, Menu
  from funcionality import menu
except ImportError:
  print('Error al importar la librerias', ImportError)


class UIMenu(Frame):
  def __init__(self, root):
    super().__init__(root)

    # Create menu
    self.bar_menu = Menu(root)
    self.menu_func = menu.FuncionalityMenu()
    self.root = root.configure(menu=self.bar_menu)

    # add options to menu
    self.options_menu_00 = Menu(self.bar_menu)
    self.options_menu_00.add_command(label='Nuevo')
    self.options_menu_00.add_command(label='Salir', command=lambda: self.menu_func.destroy(root))

    self.bar_menu.add_cascade(label='Archivo', menu=self.options_menu_00)
