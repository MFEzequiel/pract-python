# -*- coding: utf-8 -*-
try:
  import sqlite3 as sql3
  from core import config
  import pandas as pd
except ImportError as e:
  print('Error al inportar la libreria ', e)

conn = sql3.connect(config.path_db)
cr = conn.cursor()

documents = [
  ("Python", "Python es un lenguaje de programación interpretado."),
  ("SQLite", "SQLite es una base de datos ligera que no requiere servidor."),
  ("Scikit-learn", "Scikit-learn es una biblioteca de machine learning para Python."),
  ("Tkinter", "Tkinter es una biblioteca para interfaces gráficas en Python.")
]

cr.execute('''
  CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL                       
  );
''')

query_insert = 'INSERT OR IGNORE INTO documents (title, content) VALUES (?, ?)'
cr.executemany(query_insert, documents)

# 📥 Importar datos desde Excel
try:
  df = pd.read_excel(config.excel_file_path)

  # Asegúrate de que las columnas sean: 'title' y 'content'
  if 'title' not in df.columns or 'content' not in df.columns:
    data_from_excel = df[['title', 'content']].dropna().values.tolist()
    cr.executemany(query_insert, data_from_excel)
    raise ValueError("El archivo Excel debe contener las columnas 'title' y 'content'.")
    print(f"{len(data_from_excel)} registros importados desde Excel.")
  else:
    print("❌ Las columnas del archivo Excel deben ser 'title' y 'content'")
  for index, row in df.iterrows():
    cr.execute('INSERT OR IGNORE INTO documents (title, content) VALUES (?, ?)', (row['title'], row['content']))
except Exception as e:
  print('Error al importar datos desde Excel: ', e)

rows = cr.execute('SELECT title, content FROM documents')

for row in rows:
  print(row)

conn.commit()
conn.close()