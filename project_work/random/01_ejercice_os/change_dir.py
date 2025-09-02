# -*- coding: utf-8 -*-
try:
  import os
except ImportError as e:
  print('Erro al importar la libreria ', e)
  
# Cambiar el directorio de trabajo actual
def current_path():
  cwd = os.getcwd()
  
  print('Directorio de trabajo anterior')
  print(cwd, '\n')

current_path()
# retoceder una carpeta
os.chdir('../')
current_path()