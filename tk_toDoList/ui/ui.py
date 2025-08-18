try:
  from tkinter import ttk, Frame
except ImportError:
    print('Error al importar la libreria tkinter', ImportError)

class UI(Frame):
  def __init__(self, root):
    super().__init__(root)
    # Elements
    self.label_title = ttk.Label(root, text="to do list")
    
    # Positions to elements
    self.label_title.grid(column=0, row=0)
