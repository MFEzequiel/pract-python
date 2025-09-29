try:
  import os
  from pathlib import Path
except ImportError as e:
  print('Erro al importar la libreria -->', e)

cwd = os.getcwd()

custom_directory = cwd + './project_work/tk/sqlite/auto/00_sql'

directory_db = './database/folder_db'
directory_excel = './public/excel'
directory_data_db = './public/data'

name_db = 'example'
name_excel = 'example'
name_csv = 'example'
name_db_excel = 'test'
name_db_csv = 'test'

name_db = str(Path(name_db).with_suffix('.db').stem + '.db')
name_excel = str(Path(name_excel).with_suffix('.xlsx').stem + '.xlsx')
name_csv = str(Path(name_excel).with_suffix('.csv').stem + '.csv')
name_db_excel = str(Path(name_db_excel).with_suffix('.xlsx').stem + '.xlsx')
name_db_csv = str(Path(name_db_excel).with_suffix('.csv').stem + '.csv')

path_directory_db = os.path.join(custom_directory, directory_db)
path_directory_excel = os.path.join(custom_directory, directory_excel)
path_directory_datas_to_db = os.path.join(custom_directory, directory_data_db)

path_directory_file_db = os.path.join(path_directory_db, name_db)
path_directory_file_excel = os.path.join(path_directory_excel, name_excel)
path_directory_file_csv = os.path.join(path_directory_excel, name_csv)
path_directory_files_excel_to_db = os.path.join(path_directory_datas_to_db, name_db_excel)
path_directory_files_csv_to_db = os.path.join(path_directory_datas_to_db, name_db_csv)


if not os.path.exists(path_directory_db):
  os.makedirs(path_directory_db)

if not os.path.exists(path_directory_excel):
  os.makedirs(path_directory_excel)

if not os.path.exists(path_directory_datas_to_db):
  os.makedirs(path_directory_datas_to_db)

directory_files_excel = os.listdir(path_directory_datas_to_db)