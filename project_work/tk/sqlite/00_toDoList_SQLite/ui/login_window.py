try:
  from tkinter import Tk, ttk, Frame, Label, StringVar, Entry, Toplevel
except ImportError as e:
  print('Error al importar la libreria ', e)

class Login(Frame):
  def __init__(self, root=None):
    super().__init__(root)
    self.root = Toplevel(root)
    self.label_name = Label(self.root, text='Nombre')
    self.label_password = Label(self.root, text='Contraseña')

    # textbox
    self.text_name = StringVar() 
    self.text_password = StringVar() 

    self.entry_name = Entry(self.root, textvariable=self.text_name)
    self.entry_password = Entry(self.root, textvariable=self.text_password)

    # Positions
    self.label_name.grid(column=0, row=0)
    self.label_password.grid(column=0, row=0)
    self.entry_name.grid(column=0, row=0)
    self.entry_password.grid(column=0, row=0)

class Singup(Frame):
  def __init__(self, root):
    super().__init__(root)
    self.label_name = Label(root, text='Nombre')
    self.label_password = Label(root, text='Contraseña')

    # textbox
    self.text_name = StringVar() 
    self.text_password = StringVar() 

    self.entry_name = Entry(root, textvariable=self.text_name)
    self.entry_password = Entry(root, textvariable=self.text_password)

    # Positions
    self.label_name.grid(column=0, row=0)
    self.label_password.grid(column=0, row=0)
    self.entry_name.grid(column=0, row=0)
    self.entry_password.grid(column=0, row=0)