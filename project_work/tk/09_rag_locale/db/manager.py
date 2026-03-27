# -*- coding: utf-8 -*-
try:
  import os
  import sqlite3 as sql3
  from sqlite3 import Error
  from core import config
  from db import models
except ImportError as e:
  print('Erro al importar la libreria ', e)

class DAO:
  def __init__(self) -> None:
    # create folder is not exists
    if not os.path.exists(config.folder_db):
      os.mkdir(config.folder_db)
      print('Carpeta creada %s' % config.folder_db)
      
    self.connect()
  
  def connect(self):
    try:
      self.conn = sql3.connect(config.path_db)
      self.cr = self.conn.cursor()
      print('Conexion exitosa a la base de datos')
      models.ModelDB().create_table(self.conn, self.cr)

      # Documentos de ejemplo
      self.documents = [
        ("Python", "Python es un lenguaje de programación interpretado."),
        ("SQLite", "SQLite es una base de datos ligera que no requiere servidor."),
        ("Scikit-learn", "Scikit-learn es una biblioteca de machine learning para Python."),
        ("Tkinter", "Tkinter es una biblioteca para interfaces gráficas en Python.")
      ]

      # Insertar documentos de ejemplo si la tabla está vacía
      self.query = 'INSERT OR IGNORE INTO documents ( title, content) VALUES (?, ?)'
      self.cr.executemany(self.query, self.documents)

      self.conn.commit()
      print('Tabla creada exitosamente')
      self.conn.close()
    except sql3.Error as e:
      print('Error al conectar a la base de datos ', e)
  
  def get_connect(self):
    self.connect_db = {
      "conn": sql3.connect(config.path_db),
      "cr": self.conn.cursor(),
      "error": sql3.Error
    }
    return self.connect_db