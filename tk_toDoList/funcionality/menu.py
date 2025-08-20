try:
  from tkinter import messagebox
except ImportError:
  print('Error al importar la libreria', ImportError)


class FuncionalityMenu():

  def destroy(self, file_save, root):
    if not file_save:
      response = messagebox.askyesnocancel("Confirmar", "El archivo no esta guardado, ¿Desea guardarlo antes de salir?")
      if response is None:
        return
      elif response:
        file_save

    root.destroy()