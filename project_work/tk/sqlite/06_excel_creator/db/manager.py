try:
  import sqlite3 as sql
  import os
  import pandas as pd
  from core import config
except ImportError as e:
  print("Error importing module: ", e)

class ManagerDB:
  def __init__(self):
    if not os.path.exists(config.dir_path_db):
      os.makedirs(config.dir_path_db)

    self.conn = sql.connect(config.full_path_db)
    self.cr = self.conn.cursor()
    self.create_table()
    self.insert_data()

  def create_table(self):
    self.cr.execute('''
      CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        email TEXT NOT NULL UNIQUE
      )
    ''')
    self.conn.commit()

  def insert_data(self):
    
    self.insert_query = '''
      INSERT OR IGNORE INTO users (name, age, email)
      VALUES (?, ?, ?)
    '''

    self.val = [
      ('Ezeq', 12, 'ezeq@gmail'),
      ('Ana', 22, 'ana@gmail'),
      ('Luis', 32, 'luis@gmail'),
      ('Maria', 42, 'maria@gmail'),
    ]

    self.cr.executemany(self.insert_query, self.val)
    self.conn.commit()

  def get_connect(self) -> dict:
    self.dict_conn = {
      'conn': self.conn,
      'cr': self.cr
    }
    return self.dict_conn