try:
  from tkinter import Frame, Label, StringVar, Entry, Button, LabelFrame, Scrollbar, Canvas, ttk, messagebox, filedialog
except ImportError as e:
  print('Error al importar el módulo -->', e)

class Sale(Frame):
  def __init__(self, root=None) -> None:
    self.root = root
    self.widget()

  def widget(self):
    canvas_articles = LabelFrame(self.root, text='Articulos')
