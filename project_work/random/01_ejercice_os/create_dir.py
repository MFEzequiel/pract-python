# -*- coding: utf-8 -*-
try:
  import os
except ImportError as e:
  print('Erro al importar la libreria ', e)
  
# Dirección actual
cwd = os.getcwd()

# info del direcorio and join
directory = "db1"
parent_dir = cwd
path = os.path.join(parent_dir, directory)

print('directorio: ', path)

# Comprobar si existe la carpeta
if not os.path.exists(directory):
  print('\ncreate folder\n')
  os.mkdir(path)
  print('\nSe creo el directorio ( %s )\n' % directory)
else :
  print('\n exits folder \n')

# Otorgar permiso de lectura y escriturra
directory_1 = "db1"
parent_dir_1 = cwd
path_1 = os.path.join(parent_dir_1, directory_1)
# Otorgar permiso de lectura y escriturra
mode = 0o666

# Comprobar si existe la carpeta
if not os.path.exists(directory_1):
  print('\ncreate folder\n')
  os.mkdir(path, mode)
  print('\nSe creo el directorio ( %s )\n' % directory_1)
else :
  print('\n exits folder \n')