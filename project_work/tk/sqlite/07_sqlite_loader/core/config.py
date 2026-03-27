try:
  import os
  from pathlib import Path
except ImportError as e:
  print('Erro al importar la libreria -->', e)

cwd = os.getcwd()

directory_db = './db/folder_db'
directory_excel = './public/excel'
directory_data_db = './public/data'

name_db = 'example'
name_excel = 'example'
name_db_excel = 'test'

name_db = str(Path(name_db).with_suffix('.db').stem + '.db')
name_excel = str(Path(name_excel).with_suffix('.xlsx').stem + '.xlsx')
name_db_excel = str(Path(name_db_excel).with_suffix('.xlsx').stem + '.xlsx')

path_directory_db = os.path.join(cwd, directory_db)
path_directory_excel = os.path.join(cwd, directory_excel)
path_directory_datas_to_db = os.path.join(cwd, directory_data_db)

path_directory_file_db = os.path.join(path_directory_db, name_db)
path_directory_file_excel = os.path.join(path_directory_excel, name_excel)
path_directory_files_datas_to_db = os.path.join(path_directory_datas_to_db, name_db_excel)

directory_files = os.listdir(path_directory_datas_to_db)

if not os.path.exists(path_directory_db):
  os.makedirs(path_directory_db)

if not os.path.exists(path_directory_excel):
  os.makedirs(path_directory_excel)

if not os.path.exists(path_directory_datas_to_db):
  os.makedirs(path_directory_datas_to_db)
