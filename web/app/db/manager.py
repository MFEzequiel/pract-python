try:
  import os
  import sqlite3 as sql
  from core import config
except ImportError as e:
  print("Error al importar módulos. Asegúrate de tener instaladas las librerías necesarias: ", e)

class ManagerDB:
  # def __init__(self) -> None:
    # self.conn = sql.connect(config.full_path_db)
    # self.cr = self.conn.cursor()
    # if not os.path.exists(config.directory_db):
    #   os.makedirs(config.full_path_directory_folder_db)

    # self.create_table()
    # self.insert_data()
    # pass
  @staticmethod
  def create_table():
    if not os.path.exists(config.directory_db):
      os.makedirs(config.full_path_directory_folder_db)
    
    conn = sql.connect(config.full_path_db)
    cr = conn.cursor()

    cr.execute('''
      CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        email TEXT NOT NULL UNIQUE
      )
    ''')
    conn.commit()
  @staticmethod
  def insert_data():
    conn = sql.connect(config.full_path_db)
    cr = conn.cursor()
    insert_query = '''
      INSERT OR IGNORE INTO users (name, age, email)
      VALUES (?, ?, ?)
    '''

    val = [
      ('Ezeq', 12, 'ezeq@gmail'),
      ('Ana', 22, 'ana@gmail'),
      ('Luis', 32, 'luis@gmail'),
      ('Maria', 42, 'maria@gmail'),
    ]

    cr.executemany(insert_query, val)
    conn.commit()

  def _get_connect(self) -> dict:
    self.dict_conn = {
      "conn": self.conn,
      "cr": self.cr
    }
    return self.dict_conn