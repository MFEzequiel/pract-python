# -*- coding: utf-8 -*-
try:
  import os
except ImportError as e:
  print('Erro al importar la libreria ', e)

cwd = os.getcwd()
# Path folder
path = cwd
dir_list = os.listdir(path)

print(f'\nArchivos y directorios {path} :\n')
print(dir_list, '\n')