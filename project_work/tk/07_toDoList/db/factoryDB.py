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
    self.path_db = os.path.join(path_folder, name_db) 
    
    # connect to data base
    self.conn = sqlite3.connect(self.path_db)
    self.cursor = self.conn.cursor()

    # Create table example
    self.cursor.execute('''
      CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY,
        name TEXT,
        password TEXT
      )
    ''')

    # add data
    self.select_values = 'SELECT id, name, password FROM user'

    # self.exists_values = 
    # sql = 'INSERT INTO user (id, name, password) VALUES (?, ?, ?)'
    # val = [
    #   (1, 'Ezequiel', '1234'),
    #   (2, 'Ezequiel2', '124')
    # ]
    # self.cursor.executemany(sql, val)
    # Commit and close connect
    self.conn.commit()
    self.conn.close()

    print(f'Base de datos {name_db} creada en {path_folder}')
  
  def get_connection(self):
    return sqlite3.connect(self.path_db)