import os
from pathlib import Path

# Carpeta donde se guardará la base de datos
folder_db = './db/folder_db'

# Nombre y extensión correcta de la base de datos
name_db = 'empleado.db'

# Ruta completa a la base de datos
path_db = os.path.join(folder_db, name_db)

# Ruta al archivo Excel
path_excel = './public/clientes_ejemplo.xlsx'