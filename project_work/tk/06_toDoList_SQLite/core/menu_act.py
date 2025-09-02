try:
  from tkinter import messagebox
  from core import backup, file_manager
  import os
except ImportError as e:
  print('Error al importar la libreria ', e)


class FuncionalityMenu:
  def __init__(self, table=None):
    self.table = table
  def export_data_excel(self):
    if self.table:
      data = self.table.get_all_data()
      file_manager.FileManager.export_to_excel(data)

  def export_data_pdf(self):
      if self.table:
          data = self.table.get_all_data()
          file_manager.FileManager.export_to_pdf(data)

  def import_data_excel(self):
      if self.table:
          data = file_manager.FileManager.import_excel()
          if data:
              self.table.load_data(data)
          else:
              messagebox.showinfo("Importación cancelada", "No se seleccionó archivo.")
  @staticmethod
  def destroy(self, file_save, root):
    # importar local mente para evitar ciclos
    from db import factoryDB
    # Ruta de prueva del archivo db
    # TODO: hacer que el nombre de la carpeta y archivo sean dinamicos
    db_path = os.path.join('./db/folderDB', 'example.db')
    # Guardar y crear el backup
    backup = backup.BackupManager(db_path)
    backup.create_backup()

    if not file_save:
      response = messagebox.askyesnocancel("Confirmar", "El archivo no esta guardado, ¿Desea guardarlo antes de salir?")
      if response is None:
        return
      elif response:
        file_save

    root.destroy()