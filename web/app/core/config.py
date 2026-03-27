try:
  import os
  from pathlib import Path
except ImportError as e:
  print("Error al importar módulos. Asegúrate de tener instaladas las librerías necesarias: ", e)


cwd = os.getcwd()

directory_db = "./db/folder_db"
full_path_directory_folder_db = os.path.join(cwd, directory_db)

name_file_db = 'example.db'
name_file_db = str(Path(name_file_db).with_suffix('.db').stem + '.db')
full_path_db = os.path.join(full_path_directory_folder_db, name_file_db)