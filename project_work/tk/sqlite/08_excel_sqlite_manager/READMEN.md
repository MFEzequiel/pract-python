Como instalar los modulos y librerias para este proyecto
pip install -r requirements.txt

Estructura de carpetas
mi_proyecto/
│
├── core/                  # Lógica del programa (transformaciones, validaciones, etc.)
│   └── __init__.py
│   └── config.py          # variables globales
│
├── base_datos/            # Conexión, creación y CRUD con SQLite
│   └── __init__.py         
│   └── manager.py         # fabirac encargada de crear el archivo .db 
│   └── models.py          # Operaciones CRUD
│
├── main.py                 # Punto de entrada principal del programa
├── requirements.txt        # requerimiento del programa
├── READMEN.md