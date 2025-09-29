# -*- coding: utf-8 -*-
try:
  import os
  import pandas as pd 
  from core import config
  from db import manager, models
except ImportError as e:
  print('Error al importar una librería -->', e)

# Crear la carpeta donde se guardará la base de datos si no existe
if not os.path.exists(config.final_db_path):
  os.makedirs(config.final_db_path)

create_db = manager.ManagerDB()

connection = manager.ManagerDB().get_connect()['connection']
cursor = manager.ManagerDB().get_connect()['cursor']

create_table = models.ModelDB().create_table(connection, cursor) 
insert_data = models.ModelDB().insert_data(connection, cursor)