try:
  import os
  from pathlib import Path
except ImportError as e:
  print("Error al importar la libreria  -->", e)
  exit()

cwd = os.getcwd()
folder_excel = 'folder_excel_files'
folder_db = 'folder_db_files'
name_file_db = 'example.db'
name_file_excel = 'output.xlsx'

name_file_excel = str(Path(name_file_excel).with_suffix('.xlsx'))
name_file_db = str(Path(name_file_db).with_suffix('.db'))

path_folder = os.path.join(cwd,folder_excel)
path_folder_db = os.path.join(cwd,folder_db)

path_folder_files_excel = os.path.join(path_folder,name_file_excel)
path_folder_files_db = os.path.join(path_folder_db,name_file_db)

data = {
  "name": ['Eze', 'Juan','Ana'],
  "age": [25, 30, 22],
  "city": ['New York', 'Los Angeles', 'Chicago']
}

if not os.path.exists(path_folder):
  os.makedirs(path_folder)

if not os.path.exists(path_folder_db):
  os.makedirs(path_folder_db)