# -*- coding: utf-8 -*-
try:
  import os
except ImportError as e:
  print('Erro al importar la libreria ', e)

# current directory
cwd = os.getcwd()

# info to directory
directory = 'dir'
parent_dir = cwd
path = os.path.join(parent_dir, directory)

if not os.path.exists(directory):
  os.makedirs(path)
  print("\nfolder create: %s \n" % directory)
else :
  print('\n exits folder \n')

# info other directory
directory_1 = '05_folder'
parent_dir_1 = cwd + '/Ejercice'
path_1 = os.path.join(parent_dir_1, directory_1)
# Otorgar permiso de lectura y escriturra
mode = 0o666

if not os.path.exists(path_1):
  os.makedirs(path_1, mode)
  print("\nfolder create: %s \n" % directory_1)
  print(f'\nPath: {parent_dir_1}/{directory_1}\n')
else :
  print('\n exits folder \n')
  print(f'\nPath: {parent_dir_1}/{directory_1}\n')