try:
  from core import config
  import sqlite3 as sql
except ImportError as e:
  print('Error al importar una librería -->', e)

class ManagerDB:
  def __init__(self) -> None:
    # Conectar (y crear si no existe) a la base de datos SQLite
    self.connection = sql.connect(config.full_db_file_path)
    # Crear un cursor para ejecutar comandos SQL
    self.cursor = self.connection.cursor()

  def get_connect(self) -> dict:
    self.dict_connection = {
      "connection": self.connection,
      "cursor": self.cursor
    }

    return self.dict_connection