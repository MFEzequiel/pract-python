try:
  import os
  from pathlib import Path 
except ImportError as e:
  print('Erro al importar la libreria -->', e)

# Crear una nueva fila
# Agregar los nombres de la columnas
column_excel = ['Nombre', 'Edad', 'Email', 'teléfono', 'Dirección']
# Carpeta donde se guarda el excel
folder_excel = 'excel'
#Nombre del archivo
name_excel = 'data.xlsx'
# Agregar el sufijo si no lo tiene
name_excel = str(Path(name_excel).with_suffix('.xlsx'))
# Ruta del archivo excel
path_excel = os.path.join(folder_excel, name_excel)