try:
  import mysql.connector
  from mysql.connector import Error
  import os
  from dotenv import load_dotenv
except ImportError:
  print('Error al importar la librerias', ImportError)

load_dotenv()

class DAO():
  def __init__(self):
    # Leer las variables de entorno
    self.DB_HOST = os.getenv('DB_HOST', 'localhost')
    self.DB_PORT = int(os.getenv('DB_PORT', '3306'))
    self.DB_USER = os.getenv('DB_USER', 'root')
    self.DB_PASSWORD = os.getenv('DB_PASSWORD', '')
    self.DB_NAME = os.getenv('DB_NAME', 'products')
    
    try:
      self.conection = mysql.connector.connect(
        host=self.DB_HOST,
        port=self.DB_PORT,
        user=self.DB_USER,
        password=self.DB_PASSWORD,
        database=self.DB_NAME
      )

    except Error as er:
      print('Error al intetar la conexión: {0}'.format(er))
    self.list_product()
  
  def list_product(self):
    if self.conection.is_connected():
      try:   
        self.product = self.conection.cursor()
        self.product.execute('SELECT * FROM product ORDER BY ID ASC')
        self.result = self.product.fetchall()
        return self.result
      except Error as er:
        print('Error al intetar la conexión: {0}'.format(er))