# -*- coding: utf-8 -*-
try:
  import os
  from pathlib import Path
  import pandas as pd
except IndexError as e:
  print('Error al importar la libreria -->', e)

# directorio actual
cwd = os.getcwd()
# nombre de la carpeta donde guardaremos el archivo excel 
directory_excel = './public/excel'
directory_folder_excel = os.path.join(cwd, directory_excel)

# nombre del archivo excel
name_file_excel = 'example.xlsx'
# comprobar si tiene el sufigo xlsx
name_file_excel = str(Path(name_file_excel).with_suffix('.xlsx').stem + '.xlsx')
# crear el archivo excel en el directorio destino
path_file = os.path.join(directory_folder_excel, name_file_excel)

# crear la carpeta donde guardaremos el excel si no existe
if not os.path.exists(directory_folder_excel):
  os.makedirs(directory_folder_excel)

# Crear datos para agregar en el archivo de excel
students = [
  ('Ezeq', 12, 'ezeq@gmail'),
  ('Ana', 22, 'ana@gmail'),
  ('Luis', 32, 'luis@gmail'),
  ('Maria', 42, 'maria@gmail'),
]

# crear un DataFrame q es similar a una tabla
# cuenta con filas y columnas
# pd.DataFrame(datos_a_cargar, nombres_de_las_columnas)
data_file = pd.DataFrame(students, columns=['Name', 'Age', 'Email'])
print(data_file.head())

# Creaer un archivo excel
data_file.to_excel(path_file, engine='openpyxl')

rows = cursor.execute('SELECT id, name, age, email FROM students').fetchall()

data_file = pd.DataFrame(rows, columns=['Id', 'Name', 'Age', 'Email'])
print(data_file.head())

# Creaer un archivo excel
data_file.to_excel(path_file, engine='openpyxl')