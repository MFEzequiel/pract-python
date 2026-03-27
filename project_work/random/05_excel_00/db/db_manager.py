try:
  import pandas as pd
  import sqlite3 as sql
  from core import config
except ImportError as e:
  print("Error al importar la libreria -->", e)
  exit()

class DBManager:
  def __init__(self):
    self.conn = sql.connect(config.path_folder_files_db)
    self.cr = self.conn.cursor()
  
  def create_table(self):
    self.cr.execute('''
      CREATE TABLE IF NOT EXISTS clients(
        name TEXT,
        age INTEGER,
        city TEXT
      )
    ''')
    self.conn.commit()
    self.conn.close()
  
  def insert_data_from_excel(self):
    try:
      df = pd.read_excel(config.path_folder_files_excel, engine='openpyxl')
      print("Datos cargados desde Excel:")
      print(df.head())
      
      df.to_sql('clients', con=self.conn, if_exists='replace', index=False)
      print("Datos guardados en la base de datos.")
    except FileNotFoundError:
      print("❌ Archivo Excel no encontrado:", config.path_folder_files_excel)
    except Exception as e:
      print("❌ Error general:", e)

  def fetch_data(self):
    
    print("Datos en la tabla 'clients':")
    rows = self.cr.execute("SELECT name, age, city FROM clients;")
    
    for row in rows:
      print(row)
    
    self.conn.commit()
    self.conn.close()