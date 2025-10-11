try:
  from tkinter import Toplevel, Frame, RIGHT, LEFT, BOTH, Y, ttk, messagebox, filedialog 
  import os 
  import config 
  import sqlite3 as sql3 
except ImportError as e:
  print('Error al importar la librerias -->', e)

class ViewDataBase:
  def __init__(self, root) -> None:
    self.root = Toplevel(root) # Crear una nueva ventana
    self.root.title('Navegador SQLite') # Titulo de la ventana
    self.root.geometry("800x500") # Tamaño de la ventana

    # Frame principal
    self.sidebar = Frame(self.root, width=200, bg="#444") # Frame lateral
    self.sidebar.pack(side=LEFT, fill= Y) # Empaquetar el frame lateral

    self.main_panel = Frame(self.root, bg="#888") # Frame principal
    self.main_panel.pack(side=RIGHT, fill=BOTH, expand=True) # Empaquetar el frame principal

    # tree for database and table
    self.show_db = ttk.Treeview(self.sidebar) # Treeview para mostrar bases de datos y tablas
    self.show_db.pack(fill=BOTH, expand=True) # Empaquetar el treeview
    self.show_db.bind('<<TreeviewSelect>>', self.show_select) # Evento para seleccionar una tabla

    self.data_show_db = ttk.Treeview(self.main_panel) # Treeview para mostrar los datos de la tabla
    self.data_show_db.pack(fill=BOTH, expand=True) # Empaquetar el treeview

    # path --> connect
    self.databases = {}

    # Load database locale 
    self.laod_local_databases()

    if not self.databases: # Si no se encontraron bases de datos
      messagebox.showinfo("No se encontraron bases de datos", "No se encontraron bases de datos en la carpeta configurada.")


  def laod_local_databases(self):
    # Comprovar file is existe
    selected = self.show_db.focus() # Obtener el item seleccionado
    values = self.show_db.item(selected) # Obtener los valores del item seleccionado

    if not config.DIR_DB :
      print('El directorio no existe: ', config.DIR_DB) # Comprovar si el directorio existe
    
    for file in os.listdir(config.DIR_DB):
      if file.endswith('.db') or file.endswith('.sqlite'): # comprovar si el archivo es una base de datos
        self.full_path = os.path.join(config.DIR_DB, file) # obtener la ruta completa del archivo
        self.db_name = os.path.basename(self.full_path) # obtener el nombre del archivo
        self.is_path = os.path.exists(self.full_path) # comprovar si la ruta existe

        # Evitar cargar dos veces la misma base de datos
        if self.full_path in self.databases:
          continue
        
        # Si es tabla (tiene nombre de tabla y db)
        if len(values) == 2:
          config.folder_db 

        try:
          self.conn = sql3.connect(self.full_path) # conectar a la base de datos
          self.databases[self.full_path] = self.conn # guardar la conexion en un diccionario

          self.db_node = self.show_db.insert("", "end", text=self.db_name, open=True, values=[self.full_path]) # agregar la base de datos al treeview

          self.cr = self.conn.cursor() # crear un cursor
          self.cr.execute('SELECT name FROM sqlite_master WHERE type="table"') # obtener las tablas de la base de datos
          self.tables = self.cr.fetchall() # guardar las tablas en una lista

          for table in self.tables: # recorrer las tablas
            self.table_name = table[0] # obtener el nombre de la tabla
            self.show_db.insert(self.db_node, "end", text=self.table_name, values=[self.full_path, self.table_name]) # agregar la tabla al treeview
        except sql3.Error as e: 
          print(f"Error al conectar con la bbase de datos {file} ", e) 

  def show_select(self, event=None):
    # Limpiar la vista actual de datos
    for item in self.data_show_db.get_children():
        self.data_show_db.delete(item) # Eliminar cada item

    # Limpiar las columnas previas
    self.data_show_db["columns"] = () # Limpiar las columnas previas
    self.data_show_db["show"] = "" # Limpiar la vista previa

    # Obtener la tabla seleccionada
    selected = self.show_db.focus() # Obtener el item seleccionado
    values = self.show_db.item(selected)['values'] # Obtener los valores del item seleccionado
    
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
    self.cr.execute(f"PRAGMA table_info({table_name})") # Obtener la informacion de las columnas
    columns_info = self.cr.fetchall() # Guardar la informacion de las columnas en una lista
    column_names = [col[1] for col in columns_info] # Obtener los nombres de las columnas

    self.data_show_db["columns"] = column_names # Configurar las columnas
    self.data_show_db["show"] = "headings" # Mostrar solo los encabezados

    # Configurar encabezados
    for col in column_names: 
        self.data_show_db.heading(col, text=col) # Configurar el encabezado
        self.data_show_db.column(col, width=100, anchor="center") # Configurar el ancho de la columna

    try:
      self.cr.execute(f"SELECT * FROM {table_name}") # Obtener los datos de la tabla
      self.rows = self.cr.fetchall() # Guardar los datos en una lista

      # Insertar los datos
      for row in self.rows:
        self.data_show_db.insert("", "end", values=row) # Insertar los datos en el treeview
          
      # Limpiar la vista actual de datos
      for item in self.data_show_db.get_children():
        self.data_show_db.delete(item) # Eliminar cada item

      # Mostrar los datos de la tabla
      for row in self.rows:
        self.data_show_db.insert("", "end", values=row) # Insertar los datos en el treeview
    except sql3.Error as e:
      print(f"Error al consultar la tabla {table_name}: {e}")