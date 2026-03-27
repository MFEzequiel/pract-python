try:
  from tkinter import Tk, Label, StringVar, Entry, Button, ttk, messagebox
except ImportError as e:
  print('Erro al importar la libreria -->', e)

class FormCamp:
  def __init__(self) -> None:
    self.root = Tk()
    self.root.title('Fromulario de Campos')
    self.root.geometry('350x350')
    self.root.config(padx=5, pady=5)

    self.camp = []

    self.name_campo = Label(self.root, text='Nombre del Campo: ').pack(anchor='w')
    
    # Etiqueta y entrada para el nombre
    self.name_text = StringVar()
    self.name_entry = Entry(self.root, width=20, textvariable=self.name_text)
    self.name_entry.pack(pady=5)

    # Etiqueta y campo para tipo de dato
    self.label_type_data = Label(self.root, text='Tipo de dato').pack(anchor='w')
    self.data_type = ttk.Combobox(self.root, values=[
      "INT", "VARCHAR(50)", "DATE", "FLOAT", "BOOLEAN"
    ], state='readonly')
    self.data_type.pack(pady=5)
    self.data_type.current(0)

    # self.not_null

    self.bt = Button(self.root, text='+', command=self.add_camps)
    self.bt.pack(side='left', padx=5)

  def add_camps(self):
    name = self.name_entry.get()
    data_type = self.data_type.get()
    # not_null = 'si' if self.not_null.get() else: "No" 

    if not name:
      messagebox.showwarning('Advertencia', 'El nombre del campo no puede estar vacio')


    self.camp.append((name, data_type))
    print(self.camp)

  def run(self):
    self.root.mainloop()

if __name__ == '__main__':
  root = FormCamp()
  root.run()