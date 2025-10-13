try:
  from tkinter import messagebox
  from models.manager import DBManager
except ImportError as e:
  print('Error al importar la libreria ', e)

class FuncionalityMenu:
  def __init__(self, root=None, table=None, conn=None, cursor=None) -> None:
    self.root = root
    self.table = table
    self.conn = conn
    self.cursor = cursor

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

  def destroy(self, file_save):
    self.root.destroy()