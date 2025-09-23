# Intentamos importar el módulo sqlite3, que nos permite trabajar con bases de datos SQLite
try:
  import sqlite3 as sql
except ImportError as e:
  # Si ocurre un error al importar, mostramos un mensaje con el detalle del error
  print("Error al importar el módulo: ", e)

# Establecemos una conexión a la base de datos llamada 'database.db'.
# Si el archivo no existe, SQLite lo crea automáticamente.
conn = sql.connect('database.db')

# ejecutar comandos SQL en la base de datos
cr = conn.cursor()

# crear la tabla 'students' si no existe
cr.execute('''
  CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
  )
''')

# consulta para insertar datos
insert_query = "INSERT INTO students (name) VALUES (?)"
# datos a insertar
val = [
  ('John Doe'),
  ('Jane Smith'),
  ('Alice Johnson'),
  ('Bob Brown'),
]
# insertar datos en la tabla 'students'
cr.execute(insert_query, val)

# guardar los cambios en la base de datos
conn.commit()  
# mostrar el número de registros insertados
print(f"{cr.rowcount} registros insertados.")
# cerrar la conexión a la base de datos
conn.close()