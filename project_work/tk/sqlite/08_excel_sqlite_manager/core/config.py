try:
  import os
  from pathlib import Path
except ImportError as e:
  print('Error al importar una librería -->', e)

# Obtener el directorio de trabajo actual
current_directory = os.getcwd()
# Mostrar el directorio de trabajo actual
print('\n', current_directory, '\n')

# Definir una ruta base adicional si es necesario
# Sustituye el contenido entre comillas por tu ruta personalizada si aplica
custom_path = './python/sqlite/00_sql'

# Nombre y ubicación relativa de la carpeta que almacenará la base de datos
db_folder = 'db/folder_db'

# Crear ruta completa a la carpeta de base de datos (opcional)
custom_full_db_path = os.path.join(custom_path, db_folder)

# Ruta final que se usará (basada en el directorio actual)
final_db_path = os.path.join(current_directory, db_folder)

# Nombre del archivo de base de datos
db_filename = 'database'

# Asegurar que tenga extensión .db
db_filename = str(Path(db_filename).with_suffix('.db').name)

# Ruta completa del archivo de base de datos
full_db_file_path = os.path.join(final_db_path, db_filename)