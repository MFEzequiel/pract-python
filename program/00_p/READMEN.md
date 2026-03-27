Como instalar los modulos y librerias para este proyecto
  
  pip install -r requirements.txt

Estructura de Carpetas y Archivos

00_p/
│
├── config.py
├── main.py
│
├── models/
│   └── __init__.py
│   └── model_car.py
│   └── db_manager.py
│
├── views/
│   └── __init__.py
│   └── interface.py
│   └── db_viewer.py
│
├── controllers/
│   └── __init__.py
│   └── ctrl_cart.py
│
├── tests/
│   └── test_cart.py


Instrucciones para correr las pruebas

  pytest tests