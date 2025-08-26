try:
  from tkinter import Frame, Menu
  from command import menu
except ImportError:
  print('Error al importar las librerias')

class GNUMenu(Frame):
  def __init__(self, root) -> None:
    super().__init__(root)
    # function
    self.func_destroy = menu.ComandMenu()
    
    # Create menu
    self.bar_menu = Menu(root)
    self.root = root.config(menu=self.bar_menu)

    # add options to menu
    # options 1
    self.options_menu = Menu(self.bar_menu)
    self.options_menu.add_command(label='Nuevo')
    self.options_menu.add_separator()
    self.options_menu.add_command(label='Salir', command= lambda: self.func_destroy.destroy(root))
    self.bar_menu.add_cascade(label='Archivo', menu=self.options_menu)

    # options 2
    self.help_menu = Menu(self.bar_menu, tearoff=0)
    self.help_menu.add_command(label='Acerca de')
    self.bar_menu.add_cascade(label='Ayuda', menu=self.help_menu)