from sqlalchemy import create_engine
import os
from core import config

# Asegurarse de que la carpeta de la base de datos exista
os.makedirs(config.folder_db, exist_ok=True)

# Crear el engine de conexión a SQLite
engine = create_engine(f'sqlite:///{os.path.abspath(config.path_db)}')