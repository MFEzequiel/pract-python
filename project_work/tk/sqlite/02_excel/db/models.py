try:
  import os
  from core import config
except ImportError as e:
  print('Error al importar la libreria -->', e)

class Model:
  def __init__(self) -> None:
    pass

  @staticmethod
  def create_table(self, conn, cr):
    cr.execute('''
      CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        telefon TEXT,
        email TEXT
      );
    ''')
    
    conn.commit()
    conn.close()
