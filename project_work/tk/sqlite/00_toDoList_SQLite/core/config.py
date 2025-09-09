try:
  import os
  from pathlib import Path
except ImportError as e:
  print('Error al iportar la libreria -->' , e)

# directory file database
directory = './db/folder_db'
name_db = 'example.db'
folder_backups = './backups'
# Ensure the file has .db extension
name_db = str(Path(name_db).with_suffix('.db')) # erro and suffix
# Build full database file path
path_db = os.path.join(directory, name_db)