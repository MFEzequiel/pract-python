try:
  import pandas as pd
  import os
except ImportError as e:
  print('Error al importar la libreria -->', e)


class ClienteExporter:
  def __init__(self, data: dict, output_path: str, file_name: str):
    if not data:
      raise ValueError("❌ El diccionario de datos está vacío.")

    self.df = pd.DataFrame(data)

    # Convertir columna de fecha si existe
    if 'fecha_ingreso' in self.df.columns:
      self.df['fecha_ingreso'] = pd.to_datetime(self.df['fecha_ingreso'], errors='coerce')

    # Asegurar que la carpeta exista
    os.makedirs(output_path, exist_ok=True)

    # Construir paths completos
    self.excel_path = os.path.join(output_path, f"{file_name}.xlsx")
    self.csv_path = os.path.join(output_path, f"{file_name}.csv")

  def exportar(self):
    # Guardar Excel
    self.df.to_excel(self.excel_path, index=False, engine='openpyxl')

    # Guardar CSV
    self.df.to_csv(self.csv_path, index=False)

    print(f"✅ Archivos exportados:\n- Excel: {self.excel_path}\n- CSV: {self.csv_path}")

  def import_excel(self):
    pass