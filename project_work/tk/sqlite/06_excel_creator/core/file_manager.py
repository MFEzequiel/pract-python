try:
  import os
  import pandas as pd
  from core import config
  from db import manager
except ImportError as e:
  print("Error importing module: ", e)

class ClientExporte:
  def __init__(self):
    self.cr = manager.ManagerDB().get_connect()['cr']
    # Crear directorio si no existe
    if not os.path.exists(config.dir_path_excel):
      os.makedirs(config.dir_path_excel)

  def create_excel(self):
    # datos de la base de datos a excel
    self.query_select = "SELECT * FROM users"
    self.rows = self.cr.execute(self.query_select).fetchall()
    self.date_file = pd.DataFrame(self.rows, columns=['id', 'name', 'age', 'email'])
    
    # Convertir columna de fecha si existe
    if 'fecha_ingreso' in self.date_file.columns:
      self.date_file['fecha_ingreso'] = pd.to_datetime(self.date_file['fecha_ingreso'], errors='coerce')
    
    # Exportar a Excel  
    self.date_file.to_excel(config.full_path_excel, index=False, engine='openpyxl')
    
    # Exportar a CSV
    self.date_file.to_csv(config.full_path_excel.replace('.xlsx', '.csv'), index=False)