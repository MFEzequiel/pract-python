try:
  import sqlite3
  import os
except ImportError as e:
  print('Error importing libraries ', e)

class Migrator:
  def __init__(self, db_path):
    self.db_path = db_path

  def get_connection(self):
    return sqlite3.connect(self.db_path)

  def migrate(self):
    with self.get_connection() as conn:
      cursor = conn.cursor()
      
      # Verificar si la tabla de versión existe
      cursor.execute('''
        CREATE TABLE IF NOT EXISTS schema_version (
          version INTEGER PRIMARY KEY
        )
      ''')

      # Obtener versión actual
      cursor.execute('SELECT MAX(version) FROM schema_version')
      row = cursor.fetchone()
      current_version = row[0] if row and row[0] is not None else 0

      # Migración a versión 1 (ejemplo: agregar columna "email")
      if current_version < 1:
        try:
          cursor.execute("ALTER TABLE user ADD COLUMN email TEXT")
        except sqlite3.OperationalError:
          # Ya existe la columna (posible reinicio de migración)
          pass

        cursor.execute("INSERT INTO schema_version (version) VALUES (1)")
        print("Migración a versión 1 aplicada")

      conn.commit()
