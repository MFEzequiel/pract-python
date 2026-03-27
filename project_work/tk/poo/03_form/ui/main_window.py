try:
  from tkinter import Frame, messagebox, Label, Entry, Button
  from core import create_excel
except ImportError as e:
  print('Erro al importar la libreria -->', e)

class GUI(Frame):
  def __init__(self, root):
    super().__init__(root)
    # Styles
    self.label_style = {'bg': '#4B6587', 'fg': 'white'}
    self.entry_style = {'bg': '#D3D3D3', 'fg': 'black'}

    # Labels
    self.label_name = Label(root, text='Nombre', **self.label_style).grid(column=0, row=0, padx=15, pady=5)
    self.label_age = Label(root, text='Edad', **self.label_style).grid(column=0, row=1, padx=15, pady=5)
    self.label_email = Label(root, text='Email', **self.label_style).grid(column=0, row=2, padx=15, pady=5)
    self.label_telefon = Label(root, text='Teléfono', **self.label_style).grid(column=0, row=3, padx=15, pady=5)
    self.label_direction = Label(root, text='Direción', **self.label_style).grid(column=0, row=4, padx=15, pady=5)
    
    # Entries
    self.entry_name = Entry(root, **self.entry_style)
    self.entry_age = Entry(root, **self.entry_style)
    self.entry_email = Entry(root, **self.entry_style)
    self.entry_telefon = Entry(root, **self.entry_style)
    self.entry_direction = Entry(root, **self.entry_style)

    self.button = Button(root, text='guardar', bg='#6D8299', fg='white', cursor='hand2', command=lambda: create_excel.CreateFileExcel().save_data(
      self.entry_name.get(),
      self.entry_age.get(),
      self.entry_email.get(),
      self.entry_telefon.get(),
      self.entry_direction.get()
    ))

    # Positions
    self.entry_name.grid(column=1, row=0, padx=15, pady=5)
    self.entry_age.grid(column=1, row=1, padx=15, pady=5)
    self.entry_email.grid(column=1, row=2, padx=15, pady=5)
    self.entry_telefon.grid(column=1, row=3, padx=15, pady=5)
    self.entry_direction.grid(column=1, row=4, padx=15, pady=5)

    self.button.grid(column=0, row=5, padx=15, pady=5, columnspan=2)