try:
  import os
  from core import config
  import pandas as pd
  from tkinter import filedialog
  import sqlite3 as sql
except ImportError as e:
  print('Error al importar la libreria -->', e)

class Model:
  def __init__(self) -> None:
    pass

  @staticmethod
  def create_table(conn, cr):
    cr.execute('''
      CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        telefon TEXT,
        email TEXT
      );
    ''')
    
    conn.commit()
    conn.close()

  @staticmethod
  def insert_data_from_excel():
    try:
      df = pd.read_excel(config.path_folder_files_excel, engine='openpyxl')
      
      print("Datos cargados desde Excel:")
      print(df.head())

      df.to_sql('clients', con=config.engine, if_exists='replace', index=False)
      print("Datos guardados en la base de datos.")

    except FileNotFoundError:
      print("❌ Archivo Excel no encontrado:", config.path_folder_files_excel)
    except Exception as e:
      print("❌ Error general:", e)

  @staticmethod
  def load_file_excel():
    conn = sql.connect(config.path_db)
    cr = conn.cursor()
    # cargar archivos Excel
    files_path_excel = filedialog.askopenfilename(
      title="Selecciona un archivo Excel",
      filetypes=[("Archivos Excel", "*.xlsx *.xls")]
    )


    query_insert = '''
      INSERT INTO clients (name, telefon, email)
      VALUES (?, ?, ?);
    '''

    # verificar si se seleccionó un archivo
    if not files_path_excel:
      print("❌ No se seleccionó ningún archivo.")
      return
    
    print(len(files_path_excel))

    # # Procesar cada archivo Excel

    for file_path in files_path_excel:
      try:
        df = pd.read_excel(file_path, engine='openpyxl')
        
        print(f"Datos cargados desde {file_path}:")
        print(df.head())

        if 'name' not in df.columns or 'telefon' not in df.columns or 'email' not in df.columns:
          print(f"❌ El archivo {file_path} no contiene las columnas requeridas: 'name', 'telefon', 'email'.")
          continue
        else:
          # Insertar datos en la base de datos
          data_to_insert = df[['name', 'telefon', 'email']].dropna().values.tolist()
          cr.executemany(query_insert, data_to_insert)
          print(f"{len(data_to_insert)} registros importados desde {file_path}")
      except Exception as e:
        print(f"❌ Error al leer el archivo {file_path}: {e}")
        continue
    print("Importación de archivos Excel completada.")

    # # Confirmar los cambios y cerrar la conexión
    # conn.commit()
    # conn.close()
      