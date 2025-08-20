try:
  import os
  import sqlite3
except ImportError:
  print('Error al importar la librerias', ImportError)

class FactoryDB():
  def __init__(self, name_db, path_folder):
    # create foldor is not exists
    if not os.path.exists(path_folder):
      os.makedirs(path_folder)
    
    # create full path of file data base
    path_db = os.path.join(path_folder, name_db) 
    
    # connect to data base
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    # Create table example
    cursor.execute('''
      CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        password BINARY(16) TEXT NOT NULL
      )
    ''')

    # Commit and close connect
    conn.commit()
    conn.close()

    print(f'Base de datos {name_db} creada en {path_folder}')