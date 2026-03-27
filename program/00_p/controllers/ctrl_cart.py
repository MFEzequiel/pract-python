try:
  from models.model_cart import Carrito # Importar clase Carrito del modelo
  from views import interface
except ImportError as e:
  print('Error al importar el modulo en controllers -->', e)

class Controlador:
  def __init__(self, viewer=None):
    self.carrito = Carrito() # Instancia del modelo Carrito
    self.viewer = viewer # Instancia de la vista

  def add_article(self, nombre, precio):
    self.carrito.agregar_articulo(nombre, precio) # Agregar articulo al carrito
    self.viewer.actualizar_carrito(self.carrito.articulos) # Actualizar vista del carrito

  def eliminar_articulo(self, nombre):
    self.carrito.eliminar_articulo(nombre) # Eliminar articulo del carrito
    self.viewer.actualizar_carrito(self.carrito.articulos) # Actualizar vista del carrito

  def aplicar_cupon(self, porcentaje):
    self.carrito.aplicar_cupon(porcentaje) # Aplicar cupon al carrito
    self.viewer.mostrar_total(self.carrito.total()) # Mostrar total actualizado en la vista

  def finalizar_compra(self):
    total = self.carrito.finalizar_compra() # Finalizar compra y obtener total
    self.viewer.mostrar_total(total) # Mostrar total en la vista
    self.viewer.actualizar_carrito([]) # Limpiar vista del carrito
    return total
