try:
  import os
  from pathlib import Path
except ImportError as e:
  print("Error importing module: ", e)

cwd = os.getcwd()
dir_path_db = './db/folder_db'
dir_path_excel = './excel/folder_excel'

name_file_db = 'test.db'
name_file_excel = 'test.xlsx'

name_file_db = str(Path(name_file_db).with_suffix('.db').stem + '.db')
name_file_excel = str(Path(name_file_excel).with_suffix('.xlsx').stem + '.xlsx')

full_path_db = os.path.join(dir_path_db, name_file_db)
full_path_excel = os.path.join(dir_path_excel, name_file_excel)
