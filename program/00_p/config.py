try:
  import os 
  from pathlib import Path 
except ImportError as e:
  print('Error al importar el modulo -->', e)

# curren directory
cwd = os.getcwd()
#custom directory
custom_dir = os.path.join(cwd, 'program/00_p/')
# create directories if not exist
DIR_DB = os.path.join(custom_dir, 'database')
DIR_BACKUPS = os.path.join(custom_dir, 'backups')
DIR_EXCEL = os.path.join(custom_dir, 'public/excel')
DIR_DATA_EXCEL = os.path.join(custom_dir, 'public/data_excel')

for directory in [DIR_EXCEL, DIR_DB, DIR_BACKUPS, DIR_DATA_EXCEL]:
  if not os.path.exists(directory):
    os.makedirs(directory)

NAME_DB = 'cars'
NAME_EXCEL = 'data_cars'
NAME_DATA_EXCEL = os.listdir(DIR_DATA_EXCEL)

NAME_DB = str(Path(NAME_DB).with_suffix('.db').stem + '.db')
NAME_EXCEL = str(Path(NAME_EXCEL).with_suffix('.xlsx').stem + '.xlsx')

PATH_DB = os.path.join(DIR_DB, NAME_DB)
PATH_BACKUPS = os.path.join(DIR_BACKUPS, 'backups')