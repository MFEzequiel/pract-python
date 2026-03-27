try:
  from tkinter import Menu
except ImportError as e:
  print("Error importing module: ", e)

class MenuApp:
  def __init__(self, root, export_function):
    self.root = root

    self.menu = Menu(self.root)
    self.root.config(menu=self.menu)
    self.export_function = export_function 

    self.file_menu = Menu(self.menu, tearoff=0)
    self.menu.add_cascade(label="File", menu=self.file_menu)
    self.file_menu.add_command(label="Crear db", command=self.export_function)
    self.file_menu.add_separator()
    self.file_menu.add_command(label="Exit", command=self.root.quit)