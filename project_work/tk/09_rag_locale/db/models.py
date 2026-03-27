class ModelDB:
  def create_table(self, conn, c):
    c.execute("""
      CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL
      );
    """)
    conn.commit()
    conn.close()