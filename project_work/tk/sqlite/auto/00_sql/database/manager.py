try:
  from core import config
  import sqlite3 as sql
  import pandas as pd
  import os
except ImportError as e:
  print('Erro al importar la libreria -->', e)

class ManagerDB:
  def __init__(self) -> None:
    # 1. Conexión a la base de datos
    self.conn = sql.connect(config.path_directory_file_db)
    self.cursor = self.conn.cursor()
    # self.create_table()
    # self.insert_data()

  def create_table(self):
    self.cursor.execute('''
      CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
      );
    ''')
    self.conn.commit()

  def insert_data(self):
    # 2. Insertar datos de ejemplo
    query = '''
      INSERT INTO students (name, age)
      VALUES (?, ?);
    '''
    # Ejemplo de datos
    data_students = [
      ("Ezequiel", 12),
      ("Ann", 22)
    ]

    try:
      self.cursor.executemany(query, data_students)
      self.conn.commit()
    except sql.IntegrityError as e:
      print(f"Error de integridad al insertar datos: {e}")

  def insert_sqlite_type(self,dtype):
    # Convierte pandas dtype a tipos de SQLite
    if pd.api.types.is_integer_dtype(dtype):
      return "INTEGER"
    elif pd.api.types.is_float_dtype(dtype):
      return "REAL"
    elif pd.api.types.is_bool_dtype(dtype):
      return "INTEGER"
    else:
      return "TEXT"  # Por defecto, para strings y otros

  def create_table_from_excel(self, db_path, directory_files_excel):
    # 1. Listar archivos Excel en el directorio
    excel_files = [
      f for f in directory_files_excel
      if (f.endswith('.xlsx') or f.endswith('.xls')) and not f.startswith('~$') # Evitar archivos temporales
    ]

    if not excel_files:
      print("No se encontraron archivos Excel en el directorio.")
      return

    for file in excel_files:
      excel_path = os.path.join(config.path_directory_datas_to_db, file)
      table_name = os.path.splitext(file)[0].lower() # Nombre de la tabla basado en el nombre del archivo
      
      try:
        # 2. Leer el archivo Excel
        df = pd.read_excel(excel_path)

        # 3. Verificar si el DataFrame está vacío
        if df.empty:
          print(f"El archivo {file} está vacío. Saltando...")
          continue

        # 4. Crear la tabla en SQLite generar CREATE TABLE dinámicas
        columns = [col for col in df.columns if col.lower() != "id"]
        column_defs = ", ".join([f'"{col}" {self.insert_sqlite_type(df[col].dtype)}' for col in columns])

        create_table_sql = f'''
          CREATE TABLE IF NOT EXISTS "{table_name}" (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            {column_defs}
          );
        '''

        self.cursor.execute(create_table_sql)
        self.conn.commit()

        print(f"Tabla '{table_name}' creada o ya existe.")

        # 6. Evitar duplicados exactos
        existing_df = pd.read_sql_query(f'SELECT * FROM "{table_name}"', self.conn)
        new_data = df.copy()

        if not existing_df.empty:
          try:
            # 1. Eliminar columna 'id' si existe
            if "id" in existing_df.columns:
                existing_df = existing_df.drop(columns=["id"])
            if "id" in new_data.columns:
                new_data = new_data.drop(columns=["id"])

            # 2. Comparar registros por contenido completo
            new_data = new_data[~new_data.apply(tuple, axis=1).isin(existing_df.apply(tuple, axis=1))]

          except Exception as compare_error:
            print(f"No se pudo comparar registros: {compare_error}")
            continue

        if not new_data.empty:
          new_data.to_sql(table_name, self.conn, if_exists='append', index=False)
          print(f"Insertados {len(new_data)} nuevos registros en la tabla '{table_name}' desde el archivo {file}.")
        else:
          print(f"No hay nuevos datos para insertar desde el archivo {file}.")

      except Exception as e:
        print(f"Error al leer el archivo {file}: {e}")