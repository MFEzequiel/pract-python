try:
  import pandas as pd
  import os
  from pathlib import Path
  import sqlite3 as sql
  from core import config
  from db import db_manager
except ImportError:
  print("Pandas library is not installed. Please install it using 'pip install pandas' and try again.")
  exit()

df = pd.DataFrame(config.data)
print("Panda DataFrame from dictionary: \n",df)
print(df.index)

# df.to_excel(config.path_folder_files_excel,'w', index=False, replace=True, engine='openpyxl')

db_manager.DBManager().create_table()
db_manager.DBManager().insert_data_from_excel()
db_manager.DBManager().fetch_data()

conn = sql.connect(config.path_folder_files_db)
cr = conn.cursor()
rows = cr.execute("SELECT name, age, city FROM clients")
print(rows)

for row in rows:
  print(row)

conn.commit()
conn.close()