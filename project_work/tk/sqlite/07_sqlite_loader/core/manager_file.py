try:
  import os
  from pathlib import Path
  from core import config
  from db import manager, model
  import pandas as pd
except ImportError as e:
  print('Erro al importar la libreria -->', e)

class ManagerFile:
  def __init__(self) -> None:
    self.conn = manager.ManagerDB.get_connect
    self.cr = manager.ManagerDB.get_connect
    print(self.conn)

  def create_files(self):
    pass

  def insert_data_files_to_db(self):
    pass

if __name__ == '__main__':
  m = ManagerFile()