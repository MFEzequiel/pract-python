try:
  import os
  import sqlite3
  from pathlib import Path
  from core import migrator, config
except ImportError as e:
  print('Error importing libraries ', e)

class FactoryDB:
  def __init__(self, name_db, path_folder):
    # Ensure the file has .db extension
    # name_db = str(Path(name_db).with_suffix('.db')) # erro and suffix
    # Build full database file path
    # self.path_db = os.path.join(path_folder, name_db)

    # Create folder if it doesn't exist
    if not os.path.exists(config.directory):
      os.makedirs(config.directory)

    self.init_db()
    # call migration
    self.migration = migrator.Migrator(config.path_db)
    self.migration.migrate()

    print(f'Database {config.name_db} created or connected at {config.directory}')
    
  def init_db(self):
    # Connect to the database (creates file if it doesn't exist)
    self.conn = sqlite3.connect(config.path_db)
    self.cursor = self.conn.cursor()

    # Create user table if it doesn't exist
    self.cursor.execute('''
      CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY,
        name TEXT,
        password TEXT
      )
    ''')

    # Crear tabla note relacionada con user
    self.cursor.execute('''
      CREATE TABLE IF NOT EXISTS note (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        content TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
      )
    ''')

    # Save changes and close connection
    self.conn.commit()
    # self.conn.close()

    self.sql2 = 'SELECT id, name, password FROM user WHERE id=? and name=? and password=?'
    self.sql3 = 'SELECT id, title, content FROM note WHERE id=? and title=? and content=?'
    self.val2 = (1, "Ezequiel", "1234")
    self.val3 = (1, "Nota Ezequiel", "Este es el contenido de la nota")  
    self.select_user = self.cursor.execute(self.sql2, self.val2)
    self.select_note = self.cursor.execute(self.sql3, self.val3)
    self.is_user = self.cursor.fetchall()
    self.is_note = self.cursor.fetchall()
    
    if not self.is_user and not self.is_note:
      self.insert_user(1, "Ezequiel", "1234")
      self.insert_note(1, "Nota Ezequiel", "Este es el contenido de la nota")  

    self.conn.close()

  def get_connection(self):
    # Return a new database connection
    return sqlite3.connect(config.path_db)

  def insert_user(self, user_id, name, password):
    if not name or not password:
      raise ValueError("Nombre y contraseña no pueden estar vacíos.")
    if any(c in name for c in [';', '--', "'", '"']):
      raise ValueError("Nombre contiene caracteres no permitidos.")
    
    # Open a new connection
    self.conn = self.get_connection()
    self.cursor = self.conn.cursor()

    self.sql = 'INSERT INTO user (id, name, password) VALUES (?, ?, ?)'
    # Insert user into the table
    self.cursor.execute(self.sql, (user_id, name, password))

    # Save changes and close connection
    self.conn.commit()
    self.conn.close()

  def insert_note(self, user_id, title, content):
    if not title:
        raise ValueError("El título no puede estar vacío.")
    
    conn = self.get_connection()
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO note (user_id, title, content) VALUES (?, ?, ?)', (user_id, title, content))
    
    conn.commit()
    conn.close()

