import openpyxl
import os
import config as cg
from pathlib import Path

class CreateFiles:
  
  @staticmethod
  def create_excel(course='', data=''):
    file_path = os.path.join(cg.folder_files_excel, f'{course}.xlsx')

    if os.path.exists(file_path):
      wb = openpyxl.load_workbook(file_path)
      ws = wb.active
    else:
      wb = openpyxl.Workbook()
      ws = wb.active
      ws.append(['Nombre', 'Apellido', 'Curso'])
    
    ws.append(data)
    wb.save(file_path)