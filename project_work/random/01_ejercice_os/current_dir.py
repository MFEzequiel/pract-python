# -*- coding: utf-8 -*-
try:
  import os
except ImportError as e:
  print('Erro al importar la libreria ', e)

# Obtener el directorio de trabajo actual
cwd = os.getcwd()

print('Directorio actual: ', cwd)