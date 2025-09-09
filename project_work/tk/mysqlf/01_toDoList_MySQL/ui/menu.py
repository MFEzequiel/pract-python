try:
  from tkinter import Frame, Menu
  from utils.menu import FuncMenu
except ImportError:
  print('Error al inportar la libreria', ImportError)

class GUIMenu(Frame):
  def __init__(self,root):
    super().__init__(root)
    self.bar_menu = Menu(root)
    root.config(menu=self.bar_menu)

    #Inicio
    self.menu_file = Menu(self.bar_menu, tearoff=0)
    self.bar_menu.add_cascade(label='Archivo',menu=self.menu_file)
    self.menu_file.add_command(label='Crear Registro')
    self.menu_file.add_command(label='Eliminar Registro')
    self.menu_file.add_separator()
    self.menu_file.add_command(label='Salir', command=lambda: FuncMenu.exit(root))

    # Editar
    self.menu_edit = Menu(self.bar_menu, tearoff=0)
    self.bar_menu.add_cascade(label='Editar',menu=self.menu_edit)
    self.menu_edit.add_command(label='Cortar')

    # Ayuda
    self.menu_help = Menu(self.bar_menu, tearoff=0)
    self.bar_menu.add_cascade(label='Ayuda', menu=self.menu_help)
    self.menu_help.add_command(label='Acerca de')
