# -*- coding: utf-8 -*-
try:
  import os
except ImportError as e:
  print('Erro al importar la libreria ', e)

class DAO:
  def __init__(self, name_file, path_folder) -> None:
    # create folder is not exists
    if not os.path.exists(path_folder):
      os.mkdir(path_folder)
      print('Carpeta creada %s' % path_folder)