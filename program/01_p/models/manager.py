try:
  import config
  import sqlite3 as sql3
except ImportError as e:
  print('Error al importar la librerias -->', e)

class DBManager:
  def __init__(self) -> None:
    self.conn = sql3.connect(config.PATH_DB)
    self.cursor = self.conn.cursor()

  @property
  def get_connect(self) -> dict:
    self.dict_conn = {
      'conn': self.conn,
      'cursor': self.cursor
    }
    return self.dict_conn

  def close(self):
    self.conn.close()