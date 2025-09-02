try:
  import os
  import sqlite3
  from pathlib import Path
  from core import migrator
except ImportError as e:
  print('Error importing libraries:', e)

class FactoryDB:
  def __init__(self, name_db, path_folder):
    # Ensure the file has .db extension
    name_db = str(Path(name_db).with_suffix('.db'))
    # Build full database file path
    self.path_db = os.path.join(path_folder, name_db)

    # Create folder if it doesn't exist
    if not os.path.exists(path_folder):
      os.makedirs(path_folder)
      self.init_db()
       # call migration
      self.migration = migrator.Migrator(self.path_db)
      self.migration.migrate()

    print(f'Database {name_db} created or connected at {path_folder}')
    
  def init_db(self):
    # Connect to the database (creates file if it doesn't exist)
    self.conn = sqlite3.connect(self.path_db)
    self.cursor = self.conn.cursor()

    # Create user table if it doesn't exist
    self.cursor.execute('''
      CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY,
        name TEXT,
        password TEXT
      )
    ''')

    # Save changes and close connection
    self.conn.commit()
    self.conn.close()

  def get_connection(self):
    # Return a new database connection
    return sqlite3.connect(self.path_db)

  def insert_user(self, user_id, name, password):
    if not name or not password:
      raise ValueError("Nombre y contraseña no pueden estar vacíos.")
    if any(c in name for c in [';', '--', "'", '"']):
      raise ValueError("Nombre contiene caracteres no permitidos.")
    
    # Open a new connection
    conn = self.get_connection()
    cursor = conn.cursor()

    # Insert user into the table
    cursor.execute('INSERT INTO user (id, name, password) VALUES (?, ?, ?)', (user_id, name, password))

    # Save changes and close connection
    conn.commit()
    conn.close()
