try:
  import os
  from pathlib import Path
except ImportError as e:
  print('Erro al importar el modulo -->', e)

# Configuracion global
BASE_DIR = Path(__file__).resolve().parent

current_directory = os.getcwd()

custom_path = './python/sqlite/sql'
db_folder = 'db/folder_db'
directory_excel = 'public/data'

custom_full_db_path = os.path.join(custom_path, db_folder)
path_full_datas_to_db = os.path.join(custom_path, directory_excel)
directory_files = os.listdir(path_full_datas_to_db)

db_filename = 'database'
db_filename = str(Path(db_filename).with_suffix('.db').name)
full_db_file_path = os.path.join(custom_full_db_path, db_filename)