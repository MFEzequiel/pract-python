try:
  from tkinter import Frame, Menu
  import config
except ImportError as e:
  print('Error al importar el módulo -->', e)


class UIMenu(Frame):
  def __init__(self, root=None,viewDataBase=None) -> None:
    self.bar_menu = Menu(root)
    root.config(menu=self.bar_menu)

    # add option file
    self.create_options(
      self.bar_menu,
      pather_children= {
        "label": "Archivo",
        "menu": "options_file"
      },
      children= [
        {
          "label": 'Nuevo',
          "command": ''
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
          "command": lambda: viewDataBase(root)
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

  def create_options(self, pather, pather_children={}, children=[]):
    # create pather options
    option = pather_children['menu'] 
    option = Menu(pather, tearoff=0) 
    # add command
    for child in children:
      option.add_command(label=child['label'], command=child['command'])

    pather.add_cascade(label=pather_children['label'], menu=option)