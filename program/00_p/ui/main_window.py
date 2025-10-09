try:
  import os
  from core import config
  from tkinter import Frame, Label, Button, StringVar, Entry
  from db.manager import DBManager
except ImportError as e:
  print('Error al importar la librerias -->', e)

class MainGUI(Frame):
  def __init__(self, root=None):
    self.db = DBManager()
    self.form_add_product(root)
    self.form_delete_product(root)

  def form_add_product(self, root):

    self.label_title = Label(root, text='Eliminar un producto')
    self.name_product = Label(root, text='Nombre del product')
    self.product_price = Label(root, text='Precio del product')
    self.product_stock = Label(root, text='Cantidad del product')

    self.text_name = StringVar()
    self.text_price = StringVar()
    self.text_stock = StringVar()

    self.add_entry_name = Entry(root, width=20, textvariable=self.text_name)
    self.add_entry_price = Entry(root, width=20, textvariable=self.text_price)
    self.add_entry_stock = Entry(root, width=20, textvariable=self.text_stock)

    self.bt = Button(root, text='Gurdar', command=self.add_product)

    #Posición de los elementos
    self.label_title.grid(column=0, row=0)
    self.name_product.grid(column=0, row=1)
    self.product_price.grid(column=0, row=2)
    self.product_stock.grid(column=0, row=3)

    self.add_entry_name.grid(column=1, row=1)
    self.add_entry_price.grid(column=1, row=2)
    self.add_entry_stock.grid(column=1, row=3)

    self.bt.grid(column=0, row=4)

  def form_delete_product(self, root):
    self.label_title = Label(root, text='Eliminar un producto')
    self.name_product = Label(root, text='Nombre del product')
    self.product_price = Label(root, text='Precio del product')
    self.product_stock = Label(root, text='Cantidad del product')

    self.text_name = StringVar()
    self.text_price = StringVar()
    self.text_stock = StringVar()

    self.delete_entry_name = Entry(root, width=20, textvariable=self.text_name)
    self.delete_entry_price = Entry(root, width=20, textvariable=self.text_price)
    self.delete_entry_stock = Entry(root, width=20, textvariable=self.text_stock)

    self.bt = Button(root, text='Eliminar', command=self.delete_prodocut)

    #Posición de los elementos
    self.label_title.grid(column=0, row=5)
    self.name_product.grid(column=0, row=6)
    self.product_price.grid(column=0, row=7)
    self.product_stock.grid(column=0, row=8)

    self.delete_entry_name.grid(column=1, row=6)
    self.delete_entry_price.grid(column=1, row=7)
    self.delete_entry_stock.grid(column=1, row=8)

    self.bt.grid(column=0, row=9)

  def add_product(self):
    query_insert = 'INSERT INTO products (name, price, stock) VALUES (?,?,?)'

    name = self.add_entry_name.get()
    price = self.add_entry_price.get()
    stock = self.add_entry_stock.get()

    all_data = [(name, price, stock)]

    self.db.executemany(query_insert, all_data)

  def delete_prodocut(self):
    query_insert = 'DELETE FROM products WHERE name=? AND price=? AND stock=?'

    name = self.delete_entry_name.get()
    price = self.delete_entry_price.get()
    stock = self.delete_entry_stock.get()

    all_data =  [(name, price, stock)]

    self.db.executemany(query_insert, all_data)
