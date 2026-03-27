try:
  from tkinter import Frame, Label, Button, StringVar, Entry
except ImportError as e:
  print('Error al importar la librerias -->', e)

class MainGUI(Frame):
  def __init__(self, root=None, ctrl=None):
    self.root = root
    self.ctrl = ctrl
    self.form_add_product()
    self.form_delete_product()

  def form_add_product(self):

    self.label_title = Label(self.root, text='Eliminar un producto')
    self.name_product = Label(self.root, text='Nombre del product')
    self.product_price = Label(self.root, text='Precio del product')
    self.product_stock = Label(self.root, text='Cantidad del product')

    self.text_name = StringVar()
    self.text_price = StringVar()
    self.text_stock = StringVar()

    self.add_entry_name = Entry(self.root, width=20, textvariable=self.text_name)
    self.add_entry_price = Entry(self.root, width=20, textvariable=self.text_price)
    self.add_entry_stock = Entry(self.root, width=20, textvariable=self.text_stock)

    self.bt = Button(self.root, text='Gurdar', command=self.add_product)

    #Posición de los elementos
    self.label_title.grid(column=0, row=0)
    self.name_product.grid(column=0, row=1)
    self.product_price.grid(column=0, row=2)
    self.product_stock.grid(column=0, row=3)

    self.add_entry_name.grid(column=1, row=1)
    self.add_entry_price.grid(column=1, row=2)
    self.add_entry_stock.grid(column=1, row=3)

    self.bt.grid(column=0, row=4)

  def form_delete_product(self):
    self.label_title = Label(self.root, text='Eliminar un producto')
    self.id_product = Label(self.root, text='Id del product')
    self.name_product = Label(self.root, text='Nombre del product')
    self.product_price = Label(self.root, text='Precio del product')
    self.product_stock = Label(self.root, text='Cantidad del product')

    self.text_id = StringVar()
    self.text_name = StringVar()
    self.text_price = StringVar()
    self.text_stock = StringVar()

    self.delete_entry_id = Entry(self.root, width=20, textvariable=self.text_id)
    self.delete_entry_name = Entry(self.root, width=20, textvariable=self.text_name)
    self.delete_entry_price = Entry(self.root, width=20, textvariable=self.text_price)
    self.delete_entry_stock = Entry(self.root, width=20, textvariable=self.text_stock)

    self.bt = Button(self.root, text='Eliminar', command=self.delete_prodocut)

    #Posición de los elementos
    self.label_title.grid(column=0, row=5)
    self.id_product.grid(column=0, row=6)
    self.name_product.grid(column=0, row=7)
    self.product_price.grid(column=0, row=8)
    self.product_stock.grid(column=0, row=9)

    self.delete_entry_id.grid(column=1, row=6)
    self.delete_entry_name.grid(column=1, row=7)
    self.delete_entry_price.grid(column=1, row=8)
    self.delete_entry_stock.grid(column=1, row=9)

    self.bt.grid(column=0, row=10)

  def add_product(self):
    name = self.add_entry_name.get()
    price = self.add_entry_price.get()
    stock = self.add_entry_stock.get()

    if name == '' and price == '' and stock == '':
      return

    all_data = [(name, price, stock)]

    self.ctrl.add_product(all_data)

  def delete_prodocut(self):

    id_element = self.delete_entry_id.get()
    name = self.delete_entry_name.get()
    price = self.delete_entry_price.get()
    stock = self.delete_entry_stock.get()

    
    if id_element == '':
      return

    all_data =  [(id_element, name, price, stock)]

    self.ctrl.delete_product(all_data)
