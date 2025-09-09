try:
  import os
  from pathlib import Path
  import sqlite3 as sql3
  from core import config
  from db import models
except ImportError as e:
  print('Error al importar la lbreria -->', e)

class FactoryDB:
  def __init__(self):

    # create folder it doesn't exist
    if not os.path.exists(config.folder_db):
      os.makedirs(config.folder_db)

    self.conn = sql3.connect(config.path_db)
    self.c = self.conn.cursor()

    # create table and file .db or .sqlite
    models.ModelDB.create_table(self.conn, self.c)
  
  def get_connect(self):
    self.dic_connect = {
      "conn": sql3.connect(config.path_db),
      "cr": self.conn.cursor,
    }

    return self.dic_connect