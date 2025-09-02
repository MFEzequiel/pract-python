# -*- coding: utf-8 -*-
try:
    import os
except ImportError as e:
    print('Error al importar la librería:', e)

# Directorio actual
cwd = os.getcwd()

# Nombre del nuevo directorio y archivo
directory = 'db'
file_name = 'scheme.sql'

# Ruta completa del nuevo directorio
parent_dir = os.path.join(cwd, directory)

# Crear el directorio si no existe
os.makedirs(parent_dir, exist_ok=True)

# Ruta completa del archivo
file_path = os.path.join(parent_dir, file_name)

# Crear el archivo (vacío en este ejemplo)
open(file_path, 'w', encoding='utf-8')

# Mostrar la ruta del archivo
print('\nArchivo creado en:\n', file_path, '\n')
