try:
  from tkinter import ttk, Frame, Label, StringVar, Entry
  import sqlite3
  from db import factoryDB
  from core import menu_act
  from ui import table_viewer
except ImportError as e:
    print('Error al importar la libreria ', e)

class UI(Frame):
  def __init__(self, root=None):
    super().__init__(root)
    # Elements
    self.label_title = ttk.Label(root, text="to do list")

    #table
    self.table = table_viewer.Table(root)
    self.menu_func = menu_act.FuncionalityMenu(self.table)

    # Positions to elements
    self.label_title.grid(column=0, row=0)