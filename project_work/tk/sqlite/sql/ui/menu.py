try:
  from tkinter import Frame, Menu
except ImportError as e:
  print('Erro al importar el modulo -->', e)

class Menu(Frame):
  def __init__(self, root=None):

    self.menubar = Menu(root)
    self.root = root.config(menu=self.menubar)

    # add file menu
    self.file_menu = Menu(self.menubar, tearoff=0)
    self.menubar.add_cascade(label='File', menu=self.file_menu)
    self.file_menu.add_command(label='Nuevo')
    self.file_menu.add_command(label='importar Ecxel')
    self.file_menu.add_command(label='Exportar Excel')
    self.file_menu.add_separator()
    self.file_menu.add_command(label='Exit')

    # add browser sqlite
    self.sql_browser = Menu(self.menubar, tearoff=0)
    self.menubar.add_cascade(label='SQLite', menu=self.sql_browser)
    self.sql_browser.add_command(label='DB Browser')
    self.sql_browser.add_command(label='Run SQL')
    self.sql_browser.add_separator()
    self.sql_browser.add_command(label='About')
    self.sql_browser.add_command(label='Help')
    self.sql_browser.add_command(label='Exit')
    
    # add edit menu
    self.edit_menu = Menu(self.menubar, tearoff=0)
    self.menubar.add_cascade(label='Edit', menu=self.edit_menu)
    self.edit_menu.add_command(label='Undo')
    self.edit_menu.add_command(label='Redo')
