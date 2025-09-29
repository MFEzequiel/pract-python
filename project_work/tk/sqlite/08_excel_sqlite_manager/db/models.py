
class ModelDB:

  @staticmethod
  def create_table(connection, cursor):
    # Crear la tabla 'students' si no existe
    cursor.execute('''
      CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age TEXT
      )
    ''')

    # Guardar los cambios tras la creación de la tabla
    connection.commit()
    # Cerrar la conexión con la base de datos
    connection.close()

  @staticmethod
  def insert_data(connection, cursor):
    # Consulta SQL para insertar registros en la tabla students
    insert_query = 'INSERT INTO students (name, last_name, age) VALUES (?, ?, ?)'

    # Lista de estudiantes a insertar
    student_list = [
      ('John', 'Doe', '22'),
      ('Jane', 'Smit', '25'),
      ('Alice', 'Johnson', '19'),
      ('Bob', 'Brown', '34'),
    ]

    # Insertar todos los estudiantes en la base de datos
    cursor.executemany(insert_query, student_list)

    # Confirmar cambios tras la inserción
    connection.commit()
    # Cerrar la conexión con la base de datos
    connection.close()

  @staticmethod
  def show_data(connection, cursor):
    # Recuperar todos los estudiantes de la base de datos
    student_rows = cursor.execute('SELECT id, name, last_name, age FROM students').fetchall()

    # Mostrar todos los registros en consola
    print(student_rows)

    # Recorrer y mostrar cada estudiante por separado
    for row in student_rows:
      print(row)

    