try:
  import os
  from pathlib import Path
except ImportError as e:
  print('Error al importar el modulo -->', e)

# curren directory
cwd = os.getcwd()
#custom directory
custom_dir = os.path.join(cwd, 'program/00_p')

DIR_DB = os.path.join(custom_dir, 'DataBase')
DIR_BACKUPS = os.path.join(custom_dir, 'backups')
DIR_EXCEL = os.path.join(custom_dir, 'public/excel_files')
DIR_DATA_EXCEL = os.path.join(custom_dir, 'public/data_excel')

if not os.path.exists(DIR_DB):
  os.makedirs(DIR_DB)

if not os.path.exists(DIR_BACKUPS):
  os.makedirs(DIR_BACKUPS)

if not os.path.exists(DIR_DATA_EXCEL):
  os.makedirs(DIR_DATA_EXCEL)

NAME_DB = 'kiosco'
NAME_EXCEL = 'data_kiosco'
NAME_DATA_EXCEL = os.listdir(DIR_DATA_EXCEL)

NAME_DB = str(Path(NAME_DB).with_suffix('.db').stem + '.db')
NAME_EXCEL = str(Path(NAME_EXCEL).with_suffix('.xlsx').stem + '.xlsx')

PATH_DB = os.path.join(DIR_DB, NAME_DB)
PATH_BACKUPS = os.path.join(DIR_BACKUPS, 'backups')