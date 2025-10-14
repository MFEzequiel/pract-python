try:
  from abc import ABC, abstractmethod
  from modules.manager_db import DBManager
  import config
except ImportError as e:
  print('Error al importar el módulo -->', e)

class DBModel:
  def __init__(self) -> None:
    self.db = DBManager(config.DIR_FILE_DB)
    self.conn = self.db.connect_db['conn']
    self.cursor = self.db.connect_db['cursor']
    self.tables()
  
  def tables(self):
    self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        costo REAL NOT NULL,
        date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
        stock INTEGER NOT NULL,
        state TEXT NOT NULL,
        image BLOB
      );
    """)
    # self.cursor.execute("""
    #   CREATE TABLE IF NOT EXISTS clients (
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     name TEXT NOT NULL,
    #     telefon TEXT,
    #     email TEXT
    #   );
    # """)
    # self.cursor.execute("""
    #   CREATE TABLE IF NOT EXISTS solds_products (
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     sale_id INTEGER,
    #     product_id INTEGER,
    #     total INTEGER,
    #     price REAL,
    #     FOREIGN KEY (sale_id) REFERENCES sales(id),
    #     FOREIGN KEY (product_id) REFERENCES products(id)
    #   );
    # """)
    # self.cursor.execute("""
    #   CREATE TABLE IF NOT EXISTS creadits_payments (
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     sale_id INTEGER,
    #     monto REAL,
    #     data_sale TEXT,
    #     date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    #     FOREIGN KEY (sale_id) REFERENCES sale(id)
    #   );
    # """)
    # self.cursor.execute("""
    #   CREATE TABLE IF NOT EXISTS sales (
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     date_sale TEXT NOT NULL,
    #     date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    #     client_id INTEGER NOT NULL,
    #     total REAL NOT NULL,
    #     payment REAL,
    #     sale REAL,
    #     FOREIGN KEY (client_id) REFERENCES clientes(id)
    #   );
    # """)
    # self.cursor.execute("""
    #   CREATE TABLE IF NOT EXISTS roles (
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     name TEXT UNIQUE NOT NULL,
    #     date_time DATETIME DEFAULT CURRENT_TIMESTAMP
    #   );
    # """)
    # self.cursor.execute("""
    #   CREATE TABLE IF NOT EXISTS users (
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     name_user TEXT UNIQUE NOT NULL,
    #     password_hash TEXT NOT NULL,
    #     full_name TEXT,
    #     rol_id INTEGER NOT NULL,
    #     date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    #     FOREIGN KEY (rol_id) REFERENCES roles(id)
    #   );
    # """)
    # self.cursor.execute("""
    #   CREATE TABLE IF NOT EXISTS user_activities (
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     user_id INTEGER NOT NULL,
    #     action TEXT NOT NULL,
    #     data_time TEXT NOT NULL DEFAULT (datatime('now')),
    #     detail TEXT,
    #     FOREIGN KEY (user_id) REFERENCES users(id)
    #   );
    # """)
    # self.cursor.execute("""
    #   CREATE TABLE IF NOT EXISTS user_activities (
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     client_id INTEGER NOT NULL,
    #     action TEXT NOT NULL,
    #     data_time TEXT NOT NULL DEFAULT (datatime('now')),
    #     detail TEXT,
    #     FOREIGN KEY (client_id) REFERENCES clients(id)
    #   );
    # """)
    # self.cursor.execute("""
    #   CREATE TABLE IF NOT EXISTS password_recovery(
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     user_id INTEGER NOT NULL,
    #     token TEXT NOT NULL,
    #     date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    #     expiration TEXT NOT NULL,
    #     usado INTEGER NOT NULL DEFAULT 0,
    #     FOREIGN KEY (user_id) REFERENCES users(id)
    #   );
    # """)
    self.conn.commit()
    
  def excecute(self, query, params=()):
    self.cursor.execute(query, params)
    self.conn.commit()
    return self.cursor
  
  def executemany(self, query, params=()):
    self.cursor.executemany(query, params)
    self.conn.commit()
    return self.cursor

  def fetchall(self, query, params=()):
    self.cursor.execute(query, params)
    return self.cursor.fetchall()
  
  def fetchone(self, query, params=()):
    self.cursor.execute(query, params)
    return self.cursor.fetchone()
  
  def close(self):
    self.conn.close()

class BaseModel(ABC):
  def __init_(self):
    self.db = DBManager()

  @abstractmethod
  def _save(self):
    pass
  
  @abstractmethod
  def _update(self):
    pass

  @abstractmethod
  def _delete(self):
    pass

class Clients(BaseModel):
  def __init_(self, name, city, phtone, email) -> None:
    self.id = None
    self.name = name
    self.city = city
    self.phtone = phtone
    self.email = email

  # obtener client for id
  @property
  def _id(self):
    return self.id

  @property
  def _name(self):
    return self.name
  
  @_name.setter
  def _name(self, newName=''):
    if newName == '':
      return
    self.name = newName
  
  @property
  def phone(self):
    return self._phone
  
  @phone.setter
  def phone(self, newPhone):
    if not newPhone:
      raise ValueError('El telefono no puede estar vacio')
    self.phone = newPhone

  @property
  def email(self):
    return self.email

  @email.setter
  def email(self, newEmail):
    if not newEmail:
      raise ValueError('El email no puede estar vacio')
    self.email = newEmail

class Product(BaseModel):
  def __init__(self, name, price, stock, detail=''):
    super().__init__()
    self.id = None
    self.name = name
    self.price = price
    self.stock = stock
    self.detail = detail

  # Getters y setters
  @property
  def id(self):
    return self._id

  @property
  def name(self):
    return self.name

  @name.setter
  def name(self, newName):
    if not newName:
      raise ValueError("El nombre no puede estar vacío")
    self.name = newName

  @property
  def price(self):
    return self.price

  @price.setter
  def price(self, newPrice):
    if newPrice < 0:
      raise ValueError("El precio debe ser positivo")
    self.price = newPrice

  @property
  def stock(self):
    return self.stock

  @stock.setter
  def stock(self, newStock):
    if newStock < 0:
      raise ValueError("El stock debe ser positivo")
    self.stock = newStock

  @property
  def detail(self):
    return self._detail

  @detail.setter
  def detail(self, newDetail):
    self.detail = newDetail

  def save(self):
    if self._id is None:
      cursor = self.db.execute(
        "INSERT INTO products (name, price, stock, detail) VALUES (?, ?, ?, ?)",
        (self.name, self.price, self.stock, self.detail)
      )
      self._id = cursor.lastrowid
    else:
      self.db.execute(
        "UPDATE products SET name=?, price=?, stock=?, detail=? WHERE id=?",
        (self.name, self.price, self.stock, self.detail, self.id)
      )

  def delete(self):
    if self._id is not None:
      self.db.execute("DELETE FROM products WHERE id=?", (self._id,))
      self._id = None

  @classmethod
  def get_all(self):
    rows = self.db.fetchall("SELECT * FROM products")
    products = []
    for row in rows:
        prod = (row['name'], row['price'], row['stock'], row['detail'])
        prod._id = row['id']
        products.append(prod)
    return products