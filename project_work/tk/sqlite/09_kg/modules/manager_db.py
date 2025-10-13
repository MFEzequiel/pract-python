try:
  import sqlite3 as sql
except ImportError as e:
  print('Error al importar el módulo -->', e)


class DBManager:
  def __init__(self, file_db=''):
    self.conn = sql.connect(file_db)
    self.cr = self.conn.cursor()

  @property
  def connect_db(self) -> dict: 
    dict = {
      "conn" : self.conn,
      "cursor": self.cr
    }
  
    return dict
  
