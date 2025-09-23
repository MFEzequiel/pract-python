try:
  import os
  from tkinter import Frame
  from core import config
except ImportError as e:
  print("Error al importar módulos. Asegúrate de tener instaladas las librerías necesarias: ", e)


class Main_Window(Frame):
  def __init__(self, root) -> None:
    super().__init__(root)
    