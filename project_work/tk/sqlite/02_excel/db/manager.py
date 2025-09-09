try:
  import sqlite3 as sql3
  import os
  from core import config
  from db import models
except ImportError as e:
  print('Error al importar la libreria -->', e)

class FactoryDB:
  def __init__(self) -> None:
    # create folder it doesn't exist
    if not os.path.exists(config.folder_db):
      os.makedirs(config.folder_db)

    self.conn = sql3.connect(config.path_db)
    self.cr = self.conn.cursor()

    # create table and file .db or .sqlite
    models.Model.create_table(self.conn, self.cr)