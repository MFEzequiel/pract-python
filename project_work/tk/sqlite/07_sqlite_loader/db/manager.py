try:
  import sqlite3 as sql
  from core import config
except ImportError as e:
  print('Erro al importar la libreria -->', e)

class ManagerDB:
  def __init__(self) -> None:
    self.conn = sql.connect(config.path_directory_file_db)
    self.cr = self.conn.cursor()

  def create_table(self):
    self.cr.execute('''
      CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT
      )
    ''')
    self.conn.commi()
  
  def insert_data(self):
    insert_query = '''
      INSERT OR IGNORE INTO students (name, age, email)
      VALUES (?, ?, ?)
    '''
    students = [
      ('Ezeq', 12, 'ezeq@gmail'),
      ('Ana', 22, 'ana@gmail'),
      ('Luis', 32, 'luis@gmail'),
      ('Maria', 42, 'maria@gmail'),
    ] 

    self.cr.executemany(insert_query, students)
    self.conn.commit()

  def show_data(self):
    rows = self.cr.execute('SELECT name, age, email FROM students').fetchall()
    print(rows)
    for row in rows:
      print(row)

    self.conn.commit()

  def get_connect(self) -> dict:
    self.dict_conn = {
      "conn": self.conn,
      "cr": self.cr
    }
    return self.dict_conn
  
