try:
  import os
  from pathlib import Path
except ImportError as e:
  print('Error al importar la libreria', e)

folder_db = './db/folder_db'
name_db = 'example.db'
folder_backups = './backups'
# Esure the file has .db extension
name_db = str(Path(name_db).with_suffix('.db', '.sqlite')) # erro and suffix
# Build full database path
path_db = os.path.join(folder_db, name_db)