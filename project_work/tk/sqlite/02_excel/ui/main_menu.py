try:
  from tkinter import Frame, Menu
  from core import config
  from ui.db_views import ViewDataBase
  from db import models
except ImportError as e:
  print('Error al importar la libreria -->', e)

class MainMenu(Frame):
  def __init__(self, root):
    super().__init__(root)
    self.bar_menu = Menu(root)
    root.config(menu=self.bar_menu)

    # File menu
    self.file_menu = Menu(self.bar_menu, tearoff=0)
    self.file_menu.add_command(label='Exportar Excel')
    self.file_menu.add_command(label='Importar Excel', command=models.Model.load_file_excel)
    self.file_menu.add_separator()

    # add options views table db
    self.option_sql = Menu(self.bar_menu)
    self.option_sql.add_command(label='Navegador SQL', command=lambda: ViewDataBase(root))


    # Help menu
    self.help_menu = Menu(self.bar_menu, tearoff=0)
    self.help_menu.add_command(label='Acerca de...')
    
    # add cascade to menu
    self.bar_menu.add_cascade(label='Archivo', menu=self.file_menu)
    self.bar_menu.add_cascade(label='Base de datos', menu=self.option_sql) 
    self.bar_menu.add_cascade(label='Ayuda', menu=self.help_menu)