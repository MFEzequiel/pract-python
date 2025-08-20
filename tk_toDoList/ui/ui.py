try:
  from tkinter import ttk, Frame
except ImportError:
    print('Error al importar la libreria tkinter', ImportError)

class UI(Frame):
  def __init__(self, root):
    super().__init__(root)
    # Elements
    self.label_title = ttk.Label(root, text="to do list")

    #table
    self.table = ttk.Treeview(root)

    #columns
    self.table["columns"] = ('id', 'name')

    # Formate table
    

    # Positions to elements
    self.label_title.grid(column=0, row=0)
    self.table.grid(column=0, row=1)