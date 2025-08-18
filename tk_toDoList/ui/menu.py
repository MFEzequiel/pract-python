try:
  from tkinter import ttk, Frame, Menu
except ImportError:
  print('Error al importar la libreria tkinter', ImportError)


class UIMenu(Frame):
  def __init__(self, root):
    super().__init__(root)

    # Create menu
    self.bar_menu = Menu(root)
    self.root = root.configure(menu=self.bar_menu)

    # add options to menu
    self.options_menu_00 = Menu(self.bar_menu)
    self.options_menu_00.add_command(label='Nuevo')
    self.options_menu_00.add_command(label='Salir')

    self.bar_menu.add_cascade(label='Archivo', menu=self.options_menu_00)

  # def options_menu(self, body):
  #   self.options_body = Menu(body)
  #   self.options_menu.add_command(label='Nuevo')
  #   body.add_cascade(label='Archivo', menu=self.options_menu)