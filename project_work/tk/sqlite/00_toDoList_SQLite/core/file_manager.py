try:
  import pandas as pd
  from reportlab.lib.pagesizes import letter
  from reportlab.pdfgen import canvas
  from tkinter import filedialog
  import os
except ImportError as e:
  print('Error importing libraries ', e)

class FileManager:

  @staticmethod
  def export_to_excel(data):
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    if file_path:
      df = pd.DataFrame(data, columns=["ID", "Nombre", "Contraseña"])
      df.to_excel(file_path, index=False)
      print(f"Archivo Excel guardado en {file_path}")

  @staticmethod
  def export_to_pdf(data):
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if file_path:
      c = canvas.Canvas(file_path, pagesize=letter)
      width, height = letter
      y = height - 40
      for i, row in enumerate(data):
          c.drawString(40, y, f"{row[0]} | {row[1]} | {row[2]}")
          y -= 20
          if y < 50:
              c.showPage()
              y = height - 40
      c.save()
      print(f"Archivo PDF guardado en {file_path}")

  @staticmethod
  def import_excel():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
      df = pd.read_excel(file_path)
      return df.values.tolist()
    return []

