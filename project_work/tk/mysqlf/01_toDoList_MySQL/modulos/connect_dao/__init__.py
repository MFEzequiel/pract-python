# try:
#   import os
#   import mysql.connector as mc
#   from dotenv import load_dotenv
# except ImportError as e:
#   print('Error al importar la libreria', e)

# load_dotenv()

# DB_HOST = os.getenv('DB_HOST', 'localhost')
# DB_PORT = int(os.getenv('DB_PORT', '3306'))
# DB_USER = os.getenv('DB_USER', 'root')
# DB_PASSWORD = os.getenv('DB_PASSWORD', '')
# DB_NAME = os.getenv('DB_NAME', 'users')

# mydb = mc.connect(
#   host=DB_HOST,
#   port=DB_PORT,
#   user=DB_USER,
#   password=DB_PASSWORD,
#   database= DB_NAME
# )

# cursor = mydb.cursor()

# sql = 'INSERT INTO users (id, name, password) VALUES (%s, %s, %s)'
# val = (1,'Marcelo', '1244')

# cursor.execute(sql, val)
# mydb.commit()
# cursor.close()