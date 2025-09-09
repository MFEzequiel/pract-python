try:
  from tkinter import ttk, Frame
  from db import factoryDB
  from core import config
except ImportError as e:
    print('Error al importar la libreria ', e)


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

    self.db = factoryDB.FactoryDB(config.name_db, config.directory)

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
