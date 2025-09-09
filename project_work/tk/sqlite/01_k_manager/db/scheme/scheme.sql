-- productos
CREATE TABLE IF NOT EXISTS products (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  price REAL NOT NULL,
  date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
  stock INTEGER NOT NULL
);

-- clientes 
CREATE TABLE IF NOT EXISTS clients (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  telefon TEXT,
  email TEXT
);

-- productos en stock
CREATE TABLE IF NOT EXISTS stocks (

);

-- Promociones y descuentos
CREATE TABLE IF NOT EXISTS promotions (

);

-- productos vendidos
CREATE TABLE IF NOT EXISTS solds_products (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  sale_id INTEGER,
  product_id INTEGER,
  total INTEGER,
  price REAL,
  FOREIGN KEY (sale_id) REFERENCES sales(id),
  FOREIGN KEY (product_id) REFERENCES products(id)
);

-- pagos fiados
CREATE TABLE IF EXISTS creadits_payments (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  sale_id INTEGER,
  monto REAL,
  data_sale TEXT,
  date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (sale_id) REFERENCES sale(id)
);

-- ventas
CREATE TABLE IF EXISTS sales (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  date_sale TEXT NOT NULL,
  date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
  client_id INTEGER NOT NULL,
  total REAL NOT NULL,
  payment REAL,
  sale REAL,
  FOREIGN KEY (client_id) REFERENCES clientes(id)
);

-- roles de los administradoeres 
CREATE TABLE IF NOT EXISTS roles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL -- Ejemplo: 'admin', 'cajero', 'supervisor'
  date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
);

-- usario que cumplira como: 'admin', 'cajero', 'supervisor', etc.
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name_user TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  full_name TEXT,
  rol_id INTEGER NOT NULL,
  date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (rol_id) REFERENCES roles(id)
);

-- actividades del usuario
CREATE TABLE IF EXISTS user_activities (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  action TEXT NOT NULL,
  data_time TEXT NOT NULL DEFAULT (datatime('now')),
  detail TEXT,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

-- actividades del clientes
CREATE TABLE IF EXISTS user_activities (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  client_id INTEGER NOT NULL,
  action TEXT NOT NULL,
  data_time TEXT NOT NULL DEFAULT (datatime('now')),
  detail TEXT,
  FOREIGN KEY (client_id) REFERENCES clients(id)
);

-- Recuperación de contraceña
CREATE TABLE IF NOT EXISTS password_recovery(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  token TEXT NOT NULL,
  date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
  expiration TEXT NOT NULL,
  usado INTEGER NOT NULL DEFAULT 0,
  FOREIGN KEY (user_id) REFERENCES users(id)
);