# -*- coding: utf-8 -*-
try:
  import pytest
  from models import model_cart
except ImportError as e:
  print('Error al importar el modulo tests -->', e)

@pytest.fixture
def carrito():
  return model_cart.Carrito() # Instancia del carrito para pruebas

def test_agregar_articulo(carrito):
  carrito.agregar_articulo("Camiseta", 20.0) # Agregar articulo al carrito
  assert len(carrito.articulos) == 1 # Verificar que el articulo se agrego
  assert carrito.articulos[0]['nombre'] == "Camiseta" # Verificar nombre del articulo

def test_eliminar_articulo(carrito):
  carrito.agregar_articulo("Camiseta", 20.0) # Agregar articulo al carrito
  carrito.eliminar_articulo("Camiseta") # Eliminar articulo del carrito
  assert len(carrito.articulos) == 0 # Verificar que el articulo se elimino

def test_aplicar_cupon(carrito):
  carrito.agregar_articulo("Camiseta", 100.0) # Agregar articulo al carrito
  carrito.aplicar_cupon(10) # Aplicar cupon de descuento
  assert carrito.total() == 90.0 # Verificar total con descuento

def test_finalizar_compra(carrito):
  carrito.agregar_articulo("Pantalon", 50.0) # Agregar articulo al carrito
  carrito.aplicar_cupon(20) # Aplicar cupon de descuento
  total = carrito.finalizar_compra() # Finalizar compra
  assert total == 40.0 # Verificar total final
  assert len(carrito.articulos) == 0 # Verificar que el carrito esta vacio
  assert carrito.descuento == 0 # Verificar que el descuento se reseteo

if __name__ == "__main__":
  pytest.main() # Ejecutar pruebas si se corre el script directamente