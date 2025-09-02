try:
  from db.factoryDB import FactoryDB
  import pytest
except ImportError as e:
  print('Error importing libraries:', e)

def test_sql_injection_prevention(tmp_path):
    db = FactoryDB("secure_test", tmp_path)
    conn = db.get_connection()

    # Intento de inyección SQL
    malicious_name = "Robert'); DROP TABLE user;--"
    db.insert_user(99, malicious_name, "badpass")

    cursor = conn.cursor()
    cursor.execute("SELECT name FROM user WHERE id=99")
    result = cursor.fetchone()

    # La tabla no debe haberse borrado
    assert result[0] == malicious_name
    conn.close()
