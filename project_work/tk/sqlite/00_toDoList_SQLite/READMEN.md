todo_sqlite_app/
│
├── app.py                  # Archivo principal de arranque
├── requirements.txt        # (opcional) dependencias
├── README.md               # (opcional) descripción del proyecto
│
├── core/                   # Lógica principal de la aplicación
│   ├── auth.py             # Registro, login, sesión de usuario
│   ├── controller.py       # Coordinador entre UI y lógica
│   └── config.py           # Constantes globales, rutas, opciones
│
├── ui/                     # Componentes de la interfaz Tkinter
│   ├── main_window.py      # Ventana principal de la app
│   ├── db_viewer.py        # Sidebar con DB y tablas
│   ├── table_viewer.py     # Panel que muestra datos de la tabla
│   ├── login_window.py     # Login / registro de usuario
│   └── widgets.py          # Widgets personalizados (botones, estilos, etc)
│
├── db/                     # Manejo de bases de datos SQLite
│   ├── manager.py          # Clase que abre/conecta DBs
│   ├── models.py           # Operaciones SQL para tareas, usuarios, etc
│   └── schema.sql          # (opcional) script de creación de tablas
│
├── utils/                  # Funciones auxiliares reutilizables
│   ├── file_utils.py       # Crear carpetas, validar archivos, backups
│   ├── path_utils.py       # Generar rutas a DBs, backups
│   └── validators.py       # Validación de inputs (nombre, email, etc)
│
├── backups/                # Carpeta donde se guardan backups
│   └── (archivos *.db.bak, *.zip, etc)
│
├── tests/                  # Tests unitarios y de integración
│   ├── test_auth.py
│   ├── test_db.py
│   └── test_ui.py
