try:
  import os
  from openpyxl import Workbook
  from core import config
  import re
  from tkinter import messagebox
except ImportError as e:
  print('Erro al importar la libreria -->', e)

class CreateFileExcel():
  def __init__(self):
    pass

  # crear el archivo excel
  def create_excel(self):
    self.wb = Workbook()
    # hoja activa del archivo
    self.ws = self.wb.active
    # Crear una nueva fila
    # Agregar los nombres de la columnas
    self.ws.append(config.column_excel)
    # Comprovar si existe la carpeta
    if not os.path.exists(config.folder_excel):
      os.makedirs(config.folder_excel)
    
    # Guardar el archivo
    self.wb.save(config.path_excel)
  
  
  # Guardar el datos en el archivo excel
  def save_data(self, name, age, email, telfone, direction):
    if not name or not age or not email or not telfone or not direction: 
      messagebox.showerror(title='Advertencia', message='Todos los campos son obligatorios')
    elif not re.match(string=email, pattern=r"[^@]+@[^@]+\.[^@]+"): # Validar un email de manera  simple
      pass
    
