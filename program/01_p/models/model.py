class Model:
  def __init__(self, conn=None, cursor=None) -> None:
    self.conn = conn
    self.cursor = cursor

  def defaul_create_table(self, table='products'):
    self.cursor.execute(f'''
      CREATE TABLE IF NOT EXISTS {table} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price TEXT NOT NULL,
        stock TEXT NOT NULL
      )
    ''')
    self.conn.commit()

  def excecute(self, query='', params=()):
    self.cursor.execute(query, params)
    self.conn.commit()
    return self.cursor
  
  def executemany(self, query='', params=()):
    self.cursor.executemany(query, params)
    self.conn.commit()
    return self.cursor

  def fetchall(self, query='', params=()):
    self.cursor.execute(query, params)
    return self.cursor.fetchall()
  
  def fetchone(self, query='', params=()):
    self.cursor.execute(query, params)
    return self.cursor.fetchone()
