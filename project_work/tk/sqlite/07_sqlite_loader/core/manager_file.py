try:
  import pandas as pd
  from core import config
  from db import manager
except ImportError as e:
  print('Erro al importar la libreria -->', e)

class ManagerFile:
  def __init__(self) -> None:
    self.conn = manager.ManagerDB().get_connect()['conn']
    self.cr = manager.ManagerDB().get_connect()['cr']
  
  def create_files(self):
    query_select = 'SELECT id, name, age, email FROM students'
    rows = self.cr.execute(query_select).fetchall()
    df = pd.DataFrame(rows, columns=["id", "name", "age", "email"])

    # Convertir columna de fecha si existe
    if 'fecha_ingreso' in df.columns:
      df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'], errors='coerce')

    # creaer archivo excel usar openpyxl
    df.to_excel(config.path_directory_file_excel, index=False, engine='openpyxl')

  def insert_data_files_to_db(self):
    # Leer el archivo excel y usar openpyxl
    # file_excel = filedialog.askopenfilename(
    #   initialdir=config.directory,
    #   filetypes=[("Excel files", "*.xlsx *.csv")]
    # )
    print(config.directory_files)
    # df = pd.read_excel(config.path_directory_files_datas_to_db, engine='openpyxl')
    # print(df.head())

    

