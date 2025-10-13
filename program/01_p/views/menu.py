try:
  from tkinter import Frame, Menu
  from controllers import menu_act
  from views.db_viewer import  ViewDataBase
except ImportError as e:
  print('Error al importar la librerias ', e)


class UIMenu(Frame):
  def __init__(self, root=None, table=None, conn=None, cursor=None, funcionality_menu=None) -> None:
    # Create menu
    self.bar_menu = Menu(root)
    # self.menu_func = menu_act.FuncionalityMenu(root, table, conn, cursor)
    self.funcionality_menu = funcionality_menu.FuncionalityMenu(root, table, conn, cursor)

    self.root = root.config(menu=self.bar_menu)

    # add options to menu file
    self.create_options(
      self.bar_menu,
      pather_children={
        "label": "Archivo",
        "menu": "option_file"
      },
      children=[
        {
          "label": "Nuevo",
          "command": None
        },
        {
          "label": "Exportar Excel",
          "command": self.funcionality_menu.export_data_excel
        },
        {
          "label": "Exportar PDF",
          "command": self.funcionality_menu.export_data_pdf
        },
        {
          "label": "Importar Excel",
          "command": self.funcionality_menu.import_data_excel
        },
        {
          "label": "Salir",
          "command": lambda: self.funcionality_menu.destroy(root)
        }
      ]
    )

    # Add options to menu register
    self.create_options(
      self.bar_menu,
      pather_children={
        "label": "Base De Datos",
        "menu": "option_borowser_sql"
      },
      children=[
        {
          "label": "Ver Tablas",
          "command": lambda: ViewDataBase(root)
        },
        {
          "label": "Crear Tabla",
          "command": None
        },
        {
          "label": "Editar Tabla",
          "command": None
        },
        {
          "label": "Eliinar Tabla",
          "command": None
        }
      ]
    )
    
    # Add option help
    self.create_options(
      self.bar_menu,
      pather_children={
        "label": "Ayuda",
        "menu": "option_help"
      },
      children=[
        {
          "label": "Acerca de",
          "command": None
        }
      ]
    )

  def create_options(self, pather, pather_children={}, children=[]):
    # create pather options
    option = pather_children['menu'] 
    option = Menu(pather, tearoff=0) 
    # add command
    for child in children:
      option.add_command(label=child['label'], command=child['command'])

    pather.add_cascade(label=pather_children['label'], menu=option)