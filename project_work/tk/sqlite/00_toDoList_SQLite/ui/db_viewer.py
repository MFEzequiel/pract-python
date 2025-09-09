try:
  from tkinter import Toplevel, Frame, RIGHT, LEFT, BOTH, Y, ttk, messagebox, filedialog
  import os
  import sqlite3 as sq3
  from core import config
except ImportError as e:
  print('Error al importar la libreria ', e)

class ViewDataBase:
  def __init__(self, root) -> None:
    self.root = Toplevel(root)
    self.root.title('Navegador SQLite')
    self.root.geometry("800x500")

    # Frame principal
    self.sidebar = Frame(self.root, width=200, bg="#444")
    self.sidebar.pack(side=LEFT, fill= Y)

    self.main_panel = Frame(self.root, bg="#888")
    self.main_panel.pack(side=RIGHT, fill=BOTH, expand=True)

    # tree for database and table
    self.show_db = ttk.Treeview(self.sidebar)
    self.show_db.pack(fill=BOTH, expand=True)
    self.show_db.bind('<<TreeviewSellect>>', self.show_select)

    self.data_show_db = ttk.Treeview(self.main_panel)
    self.data_show_db.pack(fill=BOTH, expand=True)

    # path --> connect
    self.databases = {}
    messagebox.showinfo(self.databases)

    # Load database locale 
    self.laod_local_databases()

  def load_database(self):
    # load multiples files
    self.db_path = filedialog.askopenfilenames(filetypes=[("SQLite files", "*.db *.sqlite")])
    pass
  
  def laod_local_databases(self):
    # Comprovar file is existe
    selected = self.show_db.focus()
    values = self.show_db.item(selected)

    if not config.directory :
      print('El directorio no existe: ', config.directory) 

    for file in os.listdir(config.directory):
      if file.endswith('.db') or file.endswith('.sqlite'):
        self.full_path = os.path.join(config.directory, file)
        self.db_name = os.path.basename(self.full_path)
        self.is_path = os.path.exists(self.full_path)
        # Evitar cargar dos veces la misma base de datos
        if self.full_path in self.databases:
          continue
          
        # Si es tabla (tiene nombre de tabla y db)
        if len(values) == 2:
          config.directory

        try:
          self.conn = sq3.connect(self.full_path)
          self.databases[config.directory] = self.conn

          self.db_node = self.show_db.insert("", "end", text=self.db_name, open=True, values=[config.directory])

          self.cr = self.conn.cursor()
          self.cr.execute('SELECT name FROM sqlite_master WHERE type="table"')
          self.tables = self.cr.fetchall()

          for table in self.tables:
            self.table_name = table[0]
            self.show_db.insert(self.db_node, "end", text=self.table_name, values=[config.directory, self.table_name])
        except sq3.Error as e:
          print(f"Error al conectar con la bbase de datos {file} ", e)
          # messagebox.showinfo(f"Error al conectar con la bbase de datos {file} ", e)

  def show_select(self, event):
    pass