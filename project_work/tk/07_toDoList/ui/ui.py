try:
  from tkinter import ttk, Frame
  import sqlite3
  from db import factoryDB
except ImportError:
    print('Error al importar la libreria tkinter', ImportError)

class UI(Frame):
  def __init__(self, root):
    super().__init__(root)
    # Elements
    self.label_title = ttk.Label(root, text="to do list")

    #table
    self.table = ttk.Treeview(root, columns=('id', 'name', 'password'), show='headings')

    # Heading table
    self.table.heading('id', text='ID')
    self.table.heading('name', text='Nombre')
    self.table.heading('password', text='Contraseña')
    # value of columns
    self.display_db()

    # Positions to elements
    self.label_title.grid(column=0, row=0)
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
      self.table.insert('', 'end', values=(row[0], row[1], row[2]))

    self.conn.close()
