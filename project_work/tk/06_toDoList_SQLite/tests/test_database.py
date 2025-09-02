try:
  import os
  import sqlite3
  from db.factoryDB import FactoryDB
except ImportError as e:
  print('Error importing libraries:', e)

def test_create_and_insert_user(tmp_path):
    db_path = tmp_path / "test.db"
    db = FactoryDB("test", tmp_path)
    conn = db.get_connection()
    cursor = conn.cursor()

    db.insert_user(1, "Juan", "1234")
    cursor.execute("SELECT name FROM user WHERE id=1")
    result = cursor.fetchone()

    assert result[0] == "Juan"
    conn.close()