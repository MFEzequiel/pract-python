try:
  import sys
  import os
  from pathlib import Path
  import getpass as gp
except ImportError as e:
  print('Error al importar el módulo -->', e)

cwd = os.getcwd()
CUSTOM_PATH = os.path.join(cwd, 'project_work/tk/sqlite/09_kg')

DIR_DB = os.path.join(CUSTOM_PATH, 'data_base')
DIR_EXCEL = os.path.join(CUSTOM_PATH, 'public/excel')
DIR_DB_EXCEL = os.path.join(CUSTOM_PATH, 'public/data_excel_csv')
DIR_DB_STUDENTS =  os.path.join(CUSTOM_PATH, 'public/data_students_db')
DIR_IMAGE = os.path.join(CUSTOM_PATH, 'public/image')
DIR_TICKETS = os.path.join(CUSTOM_PATH, 'tickets')
DIR_TICKETS_IMG = os.path.join(DIR_TICKETS, 'file_image')
DIR_TICKETS_PDF = os.path.join(DIR_TICKETS, 'file_pdfs')

def create_directories():
  for directory in [DIR_DB, DIR_EXCEL, DIR_DB_EXCEL, DIR_DB_STUDENTS, DIR_TICKETS,
    DIR_TICKETS_IMG, DIR_TICKETS_PDF, DIR_IMAGE
  ]:
    if not os.path.exists(directory):
      os.makedirs(directory)

def create_folder():
  DIR_EN = os.path.join(CUSTOM_PATH, 'Encripado')
  PASSWORD = 1234
  if not os.path.exists(DIR_EN):
    os.makedirs(DIR_EN)
    try:
      with open(f"{DIR_EN}/.password", "w") as f:
        f.write(PASSWORD)
    except Exception as e:
      print("Error al crear la carpeta encriptada")


db_name = 'kisco'
name_db_excel = 'kisco'
name_db_csv = 'kisco'

db_name = str(Path(db_name).with_suffix('.db').stem + '.db')
name_db_excel = str(Path(name_db_excel).with_suffix('.xlsx').stem + '.xlsx')
name_db_csv = str(Path(name_db_csv).with_suffix('.csv').stem + '.csv')

DIR_FILE_DB = os.path.join(DIR_DB, db_name)
DIR_FILE_EXCEL_TO_DB = os.path.join(DIR_DB_EXCEL, name_db_excel)
DIR_FILE_CSV_TO_DB = os.path.join(DIR_DB_EXCEL, name_db_csv)