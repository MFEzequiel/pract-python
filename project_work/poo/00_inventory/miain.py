class Products:
  # Productos
  def __init__(self, id, name=None, price=None, stok=None) -> None:
    self.id = id
    self.name = name
    self.price = price
    self.stok = stok

  def __str__(self):
    return f'{self.name}, (ID: {self.id}, price: {self.price}, stok: {self.stok})'

class Inventary:
  def __init__(self) -> None:
    self.products = {}

  # agregar productos
  def add_product(self, product):
    if product.id in self.products:
      print("El producto ya existe")
      # Actualizar la cantidad
      self.products[product.id].stok += product.stok
    else:
      # Agregar el producto
      self.products[product.id] = product
      print("Producto agregado")
  
  def delte_product(self, id):
    if id in self.products:
      del self.products[id]
      print(f'Producto con ID {id} eliminado')
    else:
      print(f'Producto no encontrado')
  
  def update_product(self, id, name=None, price=None, stok=None):
    if id in self.products:
      if name:
        self.products[id].name = name
      if price:
        self.products[id].price = price
      if stok:
        self.products[id].stok = stok
      print(f'Producto con ID {id} actualizado')
    else:
      print(f'Producto no encontrado')

  def list_products(self):
    for product in self.products.values():
      print(product)

inventary_one = Inventary()
product_one = Products(1, 'Manzana', 0.50, 100)
product_two = Products(2, 'Pera', 0.50, 100)

print('\n')
inventary_one.add_product(product_one)
inventary_one.add_product(product_two)
print('\n')
inventary_one.list_products()
print('\nActualización de productos\n')
inventary_one.update_product(1, price=0.75, stok=150)
print('\n')
inventary_one.list_products()
print('\n')
