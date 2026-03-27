try:
  import os
  from pathlib import Path
except ImportError as e:
  print('Error al importar la lbreria -->', e)

folder_db = './db/falderDB'
name_file_db = 'database.db'
excel_file_path = './data/'
name_file_db = str(Path(name_file_db).with_suffix('.db'))
excel_file_path = str(Path(excel_file_path).with_suffix('.xlsx'))
path_db = os.path.join(folder_db, name_file_db)