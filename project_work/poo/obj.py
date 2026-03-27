try:
  import os
  import sys
  import sqlite3 as sql
  from pathlib import Path
  from abc import ABC, abstractmethod
except ImportError as e:
  print('Error al importar la libreria -->', e)

class Config:
  def __init__(self) -> None:
    self.cwd = os.getcwd()
    self.custom_path = os.path.join(self.cwd, 'project_worck', 'poo')
    self.path_files_db = os.path.join(self.cwd, 'project_worck', 'poo', 'db')
    self.dir_db = ''
    # Crear carpeta oculta
    self.folder_ocult(self.path_files_db)
    # Archivos    
    self.db_name = 'kiosco'
    # Comprobar las extenciones
    self.db_name = str(Path(self.db_name).with_suffix('.db').stem + '.db')
    # Carpeta donde se guardo los archivos
    self.dir_file_db = os.path.join(self.dir_db, self.db_name)

    self.default_files('kiosco','kiosco','kiosco')

  # Método encargado de ocultar la carpeta 
  # donde se guardara la db
  def folder_ocult(self, folder_db):
    if sys.platform == 'win32':
      import ctypes
      if not os.path.exists(folder_db):
        os.makedirs(folder_db)
        a = ctypes.windll.kernel32.SetFileAttributesW(folder_db, 0x02)
      self.dir_db = os.path.join(self.custom_path, folder_db)
    else:
      name = os.path.join('.', folder_db)
      folder = os.path.join(self.custom_path, name)
      if not os.path.exists(folder):
        os.makedirs(folder)
      self.dir_db = os.path.join(self.custom_path, folder_db)

class DBManager:
  def __init__(self, file_db=''):
    self.file_db = file_db
    self.conn = sql.connect(self.file_db)
    self.cursor = self.conn.cursor()

  def excecute_all(self, query):
    self.cursor.execute(query)
    self.conn.commit()
    return self.cursor
  
  def excecute(self, query, params=()):
    self.cursor.execute(query, params or [])
    self.conn.commit()
    return self.cursor
  
  def executemany(self, query, params=()):
    self.cursor.executemany(query, params or [])
    self.conn.commit()
    return self.cursor

  def fetchall_all(self, query):
    self.cursor.execute(query)
    return self.cursor.fetchall()

  def fetchall(self, query, params=()):
    self.cursor.execute(query, params or [])
    return self.cursor.fetchall()
  
  def fetchone_all(self, query):
    self.cursor.execute(query)
    return self.cursor.fetchone()

  def fetchone(self, query, params=()):
    self.cursor.execute(query, params or [])
    return self.cursor.fetchone()

  def close(self):
    self.conn.close()

# Definir como van a ser y que van a contener los objetos que creamos
class Users:
  def __init__(self, fullname, user, age, password):
    self.fullname = fullname # Atributo público
    self.user = user # Atributo público
    self.__password = password # Atributo muy privado
    self.age = age # Atributo público

  # getter
  @property
  def name_user(self):
    return self.__password
  
  # setter
  @name_user.setter
  def name_user(self, new_password):
    self.__password = new_password

class Phone(ABC):
  def __init__(self, model, marca, camera, read_camera, front_camera) -> None:
    self.model = model
    self.marca = marca
    self.camera = camera
    self.read_camera = read_camera
    self.front_camera = front_camera

  @abstractmethod
  def more_info(self):
    pass

class Smartphone(Phone):
  def __init__(self, model, marca, camera, read_camera, front_camera, gps, bluetooth) -> None:
    Phone.__init__(model, marca, camera, read_camera, front_camera)
    self.gps = gps
    self.bluetooth = bluetooth

  # Implementación obligatoria del métodod abstracto
  def more_info(self):
    return print(f'Model: {self.model},
      Marca: {self.marca},
      Camara: {self.camera},
      Camara Trasera: {self.read_camera},
      Camara Frontal: {self.front_camera},
      GPS: {self.gps},
      Bluetooth: {self.bluetooth}'
    )

class Cars(ABC):
  def __init__(self, marca, modelo, puertas, tipo) -> None:
    self.marca = marca
    self.modelo = modelo
    self.puertas = puertas
    self.tipo = tipo

  @abstractmethod
  def more_info(self):
    pass

class Smartphone(Cars):
  def __init__(self, marca, modelo, puertas, tipo, gps, bluetooth) -> None:
    Cars.__init__(marca, modelo, puertas, tipo)
    self.gps = gps
    self.bluetooth = bluetooth

  # Implementación obligatoria del métodod abstracto
  def more_info(self):
    return print(f'Model: {self.modelo},
      Modelo: {self.modelo},
      Marca: {self.marca},
      Puertas N°: {self.puertas},
      Tipo: {self.tipo},
      GPS: {self.gps},
      Bluetooth: {self.bluetooth}'
    )