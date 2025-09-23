import pandas as pd
from core import config
from db.engine import engine

def cargar_excel_y_guardar():
  try:
    # Leer el archivo Excel
    df = pd.read_excel(config.path_excel, engine='openpyxl')

    # Verificar que se leyó correctamente
    print("Datos cargados desde Excel:")
    print(df.head())

    # Guardar los datos en la base de datos
    df.to_sql('clients', con=engine, if_exists='replace', index=False)
    print("Datos guardados en la base de datos.")
  except FileNotFoundError:
    print("❌ Archivo Excel no encontrado:", config.path_excel)
  except Exception as e:
    print("❌ Error general:", e)

if __name__ == "__main__":
  cargar_excel_y_guardar()