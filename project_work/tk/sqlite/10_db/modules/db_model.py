try:
  import os
except ImportError as e:
  print('Error al importar el módulo -->', e)

class DBModel:
  def __init__(self):
    self.db_path = None
    self.conn = None

    def open_db(self, path):
      pass