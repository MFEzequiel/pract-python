try:
  import os
  from core import config
  import sqlite3 as sql3
except ImportError as e:
  print('Error al importar la librerias -->', e)

class DBManager:
  def __init__(self) -> None:
    self.conn = sql3.connect(config.PATH_DB)
    self.cursor = self.conn.cursor()

    self.create_table()

  def create_table(self):
    self.cursor.execute('''
      CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price TEXT NOT NULL,
        stock TEXT NOT NULL
      )
    ''')
    self.conn.commit()

  def excecute(self, query, params=()):
    self.cursor.execute(query, params)
    self.conn.commit()
    return self.cursor
  
  def executemany(self, query='', params=()):
    self.cursor.executemany(query, params)
    self.conn.commit()
    return self.cursor

  def fetchall(self, query, params=()):
    self.cursor.execute(query, params)
    return self.cursor.fetchall()
  
  def fetchone(self, query, params=()):
    self.cursor.execute(query, params)
    return self.cursor.fetchone()

  def get_connect(self) -> dict:
    self.dict_conn = {
      'conn': self.conn,
      'cursor': self.cursor
    }
    return self.dict_conn

  def close(self):
    self.conn.close()