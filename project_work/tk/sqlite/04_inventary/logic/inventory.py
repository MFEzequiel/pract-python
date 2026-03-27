def agregar_producto(inventario, id, nombre, precio, stock):
  if id in inventario:
    return f"Producto ya existe. Se actualizó el stock."
  else:
    inventario[id] = {
      'nombre': nombre,
      'precio': precio,
      'stock': stock
    }
    return "Producto agregado."

def eliminar_producto(inventario, id):
  if id in inventario:
    del inventario[id]
    return f"Producto con ID {id} eliminado."
  else:
    return "Producto no encontrado."

def actualizar_producto(inventario, id, nombre=None, precio=None, stock=None):
  if id in inventario:
    if nombre is not None:
      inventario[id]['nombre'] = nombre
    if precio is not None:
      inventario[id]['precio'] = precio
    if stock is not None:
      inventario[id]['stock'] = stock
    return f"Producto con ID {id} actualizado."
  else:
    return "Producto no encontrado."

def listar_productos(inventario):
  return [
    f"{p['nombre']} (ID: {id}, Precio: {p['precio']}, Stock: {p['stock']})"
    for id, p in inventario.items()
  ]
