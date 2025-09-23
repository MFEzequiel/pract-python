try:
  import os
  from pathlib import Path
except ImportError as e:
  print('Error al importar la libreria -->', e)

title_app = 'Gestión de empleados'
size_app = '600x400'
folder_db = './db/folder_db'
name_db = 'empleado.db'
dinamic_name_db = Path('empleado').stem + '.db'
excel_file_path = './public/empleados.xlsx'

# Esure the file has .db extension
name_db = str(Path(name_db).with_suffix('.db'))
excel_file_path = str(Path(excel_file_path).with_suffix('.xlsx'))

# Build full database path
path_db = os.path.join(folder_db, name_db)