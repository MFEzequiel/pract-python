try:
  from tkinter import Toplevel, Frame, RIGHT, LEFT, BOTH, Y, ttk, messagebox, filedialog
  import os
  from core import config
  import sqlite3 as sql3
except ImportError as e:
  print('Error al importar la librerias -->', e)

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
    self.show_db.bind('<<TreeviewSelect>>', self.show_select)

    self.data_show_db = ttk.Treeview(self.main_panel)
    self.data_show_db.pack(fill=BOTH, expand=True)

    # path --> connect
    self.databases = {}

    # Load database locale 
    self.laod_local_databases()

    if not self.databases:
      messagebox.showinfo("No se encontraron bases de datos", "No se encontraron bases de datos en la carpeta configurada.")


  def laod_local_databases(self):
    # Comprovar file is existe
    selected = self.show_db.focus()
    values = self.show_db.item(selected)

    if not config.path_directory_db :
      print('El directorio no existe: ', config.path_directory_db) 
    
    for file in os.listdir(config.path_directory_db):
      if file.endswith('.db') or file.endswith('.sqlite'):
        self.full_path = os.path.join(config.path_directory_db, file)
        self.db_name = os.path.basename(self.full_path)
        self.is_path = os.path.exists(self.full_path)

        # Evitar cargar dos veces la misma base de datos
        if self.full_path in self.databases:
          continue
        
        # Si es tabla (tiene nombre de tabla y db)
        if len(values) == 2:
          config.folder_db

        try:
          self.conn = sql3.connect(self.full_path)
          self.databases[self.full_path] = self.conn

          self.db_node = self.show_db.insert("", "end", text=self.db_name, open=True, values=[self.full_path])

          self.cr = self.conn.cursor()
          self.cr.execute('SELECT name FROM sqlite_master WHERE type="table"')
          self.tables = self.cr.fetchall()

          for table in self.tables:
            self.table_name = table[0]
            self.show_db.insert(self.db_node, "end", text=self.table_name, values=[self.full_path, self.table_name])
        except sql3.Error as e:
          print(f"Error al conectar con la bbase de datos {file} ", e)
          # messagebox.showinfo(f"Error al conectar con la bbase de datos {file} ", e)

  def show_select(self, event=None):
    # Limpiar la vista actual de datos
    for item in self.data_show_db.get_children():
        self.data_show_db.delete(item)

    # Limpiar las columnas previas
    self.data_show_db["columns"] = ()
    self.data_show_db["show"] = ""

    # Obtener la tabla seleccionada
    selected = self.show_db.focus()
    values = self.show_db.item(selected)['values']
    
    if len(values) < 2:  # Verifica que haya una base de datos y una tabla seleccionada
      return

    db_path = values[0]  # Ruta de la base de datos
    table_name = values[1]  # Nombre de la tabla

    # Conectar a la base de datos seleccionada
    conn = self.databases.get(db_path)
    if not conn:
      print(f"Error: No se pudo encontrar la base de datos {db_path}")
      return

    # Mostrar los datos de la tabla
    # Obtener nombres de columnas
    self.cr.execute(f"PRAGMA table_info({table_name})")
    columns_info = self.cr.fetchall()
    column_names = [col[1] for col in columns_info]

    self.data_show_db["columns"] = column_names
    self.data_show_db["show"] = "headings"

    # Configurar encabezados
    for col in column_names:
        self.data_show_db.heading(col, text=col)
        self.data_show_db.column(col, width=100, anchor="center")

    try:
      self.cr.execute(f"SELECT * FROM {table_name}")
      self.rows = self.cr.fetchall()

      # Insertar los datos
      for row in self.rows:
        self.data_show_db.insert("", "end", values=row)
          
      # Limpiar la vista actual de datos
      for item in self.data_show_db.get_children():
        self.data_show_db.delete(item)

      # Mostrar los datos de la tabla
      for row in self.rows:
        self.data_show_db.insert("", "end", values=row)
    except sql3.Error as e:
      print(f"Error al consultar la tabla {table_name}: {e}")