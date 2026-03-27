try:
  from db import manager
  from core import manager_file
  import pandas as pd
except ImportError as e:
  print('Erro al importar la libreria -->', e)

conn = manager.ManagerDB()
mf = manager_file.ManagerFile()
mdc = conn.create_table()
mfd = mf.insert_data_files_to_db()
# crdf = mf.create_files()
show_data = conn.show_data()
print(mfd)