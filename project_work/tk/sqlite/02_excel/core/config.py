try:
  import os
  from pathlib import Path
except ImportError as e:
  print('Error al importar la libreria -->', e)


folder_db = './db/folder_db'
name_db = 'empleado.db'
dinamic_name_db = Path('empleado').stem + '.db'
path_excel = './public/empleados.xlsx'
# Esure the file has .db extension
name_db = str(Path(name_db).with_suffix('.db'))
# Build full database path
path_db = os.path.join(folder_db, name_db)