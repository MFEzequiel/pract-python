try:
  from tkinter import ttk, Frame, Label, StringVar, Entry
  import sqlite3
  from db import factoryDB
  from core import menu_act
except ImportError:
    print('Error al importar la libreria tkinter', ImportError)

class Table(Frame):
  def __init__(self, root):
    super().__init__(root)
    #table
    self.table = ttk.Treeview(root, columns=('id', 'name', 'password'), show='headings')

    # Heading table
    self.table.heading('id', text='ID')
    self.table.heading('name', text='Nombre')
    self.table.heading('password', text='Contraseña')
    # value of columns
    self.display_db()

    # Positions to elements
    self.table.grid(column=0, row=1)
  
  def display_db(self):
    # db
    self.name_db = 'example.db'
    self.folder = './db/folderDB'

    self.db = factoryDB.FactoryDB(self.name_db, self.folder)

    self.conn = self.db.get_connection()
    self.cursor = self.conn.cursor()
    self.cursor.execute('SELECT id, name, password FROM user')

    self.rows = self.cursor.fetchall()

    for row in self.rows:
      self.table.insert('', 'end', values=(row))

    self.conn.close()

  def get_all_data(self):
    return [self.table.item(item)['values'] for item in self.table.get_children()]

  def load_data(self, data):
    for row in self.table.get_children():
      self.table.delete(row)
    for row in data:
      self.table.insert('', 'end', values=row)

class Login(Frame):
  def __init__(self, root):
    super().__init__(root)
    self.label_name = Label(root, text='Nombre')
    self.label_password = Label(root, text='Contraseña')

    # textbox
    self.text_name = StringVar() 
    self.text_password = StringVar() 

    self.entry_name = Entry(root, textvariable=self.text_name)
    self.entry_password = Entry(root, textvariable=self.text_password)

    # Positions
    self.label_name.grid(column=0, row=0)
    self.label_password.grid(column=0, row=0)
    self.entry_name.grid(column=0, row=0)
    self.entry_password.grid(column=0, row=0)

class Singup(Frame):
  def __init__(self, root):
    super().__init__(root)
    self.label_name = Label(root, text='Nombre')
    self.label_password = Label(root, text='Contraseña')

    # textbox
    self.text_name = StringVar() 
    self.text_password = StringVar() 

    self.entry_name = Entry(root, textvariable=self.text_name)
    self.entry_password = Entry(root, textvariable=self.text_password)

    # Positions
    self.label_name.grid(column=0, row=0)
    self.label_password.grid(column=0, row=0)
    self.entry_name.grid(column=0, row=0)
    self.entry_password.grid(column=0, row=0)

class UI(Frame):
  def __init__(self, root):
    super().__init__(root)
    # Elements
    self.label_title = ttk.Label(root, text="to do list")

    #table
    self.table = Table(root)
    self.menu_func = menu_act.FuncionalityMenu(self.table)


    # Positions to elements
    self.label_title.grid(column=0, row=0)