class Carrito:
  def __init__(self):
    self.articulos = [] # Lista de articulos en el carrito
    self.descuento = 0 # Descuento aplicado al carrito

  def agregar_articulo(self, nombre, precio):
    self.articulos.append({'nombre': nombre, 'precio': precio}) # Agregar articulo al carrito

  def eliminar_articulo(self, nombre):
    self.articulos = [a for a in self.articulos if a['nombre'] != nombre] # Eliminar articulo del carrito

  def aplicar_cupon(self, porcentaje):
    self.descuento = porcentaje # Aplicar descuento al carrito

  def total(self):
    total = sum(a['precio'] for a in self.articulos) # Calcular total del carrito
    return total * (1 - self.descuento / 100) # Aplicar descuento al total

  def finalizar_compra(self):
    total = self.total() # Obtener total del carrito
    self.articulos.clear() # Limpiar carrito
    self.descuento = 0 # Resetear descuento
    return total
