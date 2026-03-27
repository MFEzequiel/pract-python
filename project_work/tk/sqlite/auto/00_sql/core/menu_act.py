try:
  from tkinter import messagebox
  # from core import file_manager
  import os
except ImportError as e:
  print('Error al importar la libreria ', e)


class FuncionalityMenu:
  def __init__(self, table=None):
    self.table = table
  
  def export_data_excel(self):
    # if self.table:
    #   data = self.table.get_all_data()
    #   file_manager.FileManager.export_to_excel(data)
    pass
  
  def export_data_pdf(self):
    # if self.table:
    #   data = self.table.get_all_data()
    #   file_manager.FileManager.export_to_pdf(data)
    pass
  
  def import_data_excel(self):
    # if self.table:
    #   data = file_manager.FileManager.import_excel()
    #   if data:
    #     self.table.load_data(data)
    #   else:
    #     messagebox.showinfo("Importación cancelada", "No se seleccionó archivo.")
    pass

  def destroy(self, file_save, root=None):
    # importar local mente para evitar ciclos
    # from database import manager
    # Ruta de prueva del archivo db
    # TODO: hacer que el nombre de la carpeta y archivo sean dinamicos
    # self.db_path = os.path.join('./db/folderDB', 'example.db')
    # self.cwd = os.getcwd()
    # self.parent_dir = self.cwd + 'db' + 'folderDB' 
    # self.db_path1 = os.path.join(self.parent_dir, 'example.db')
    # print('\n',self.db_path1, '\n')
    # print('\n',root, '\n')
    # Guardar y crear el backup
    # self.backup = backup.BackupManager(self.db_path)
    # self.backup.create_backup()

    # if not file_save:
    #   response = messagebox.askyesnocancel("Confirmar", "El archivo no esta guardado, ¿Desea guardarlo antes de salir?")
    #   if response is None:
    #     return
    #   elif response:
    #     file_save

    root.destroy()