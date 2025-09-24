try:
  import sqlite3 as sql
  from core import config
except ImportError as e:
  print('Erro al importar la libreria -->', e)
