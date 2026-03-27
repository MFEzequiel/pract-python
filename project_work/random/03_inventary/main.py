# Inventario: Diccionario donde la clave es el ID del producto
inventario = {}

# Agregar producto
def agregar_producto(inventario, id, nombre, precio, stock):
    if id in inventario:
        print("El producto ya existe. Actualizando stock.")
        inventario[id]['stock'] += stock
    else:
        inventario[id] = {
            'nombre': nombre,
            'precio': precio,
            'stock': stock
        }
        print("Producto agregado.")

# Eliminar producto
def eliminar_producto(inventario, id):
    if id in inventario:
        del inventario[id]
        print(f'Producto con ID {id} eliminado.')
    else:
        print('Producto no encontrado.')

# Actualizar producto
def actualizar_producto(inventario, id, nombre=None, precio=None, stock=None):
    if id in inventario:
        if nombre is not None:
            inventario[id]['nombre'] = nombre
        if precio is not None:
            inventario[id]['precio'] = precio
        if stock is not None:
            inventario[id]['stock'] = stock
        print(f'Producto con ID {id} actualizado.')
    else:
        print('Producto no encontrado.')

# Listar productos
def listar_productos(inventario):
    if not inventario:
        print("Inventario vacío.")
    for id, producto in inventario.items():
        print(f"{producto['nombre']}, (ID: {id}, precio: {producto['precio']}, stock: {producto['stock']})")

# --- Pruebas ---
print('\n')
agregar_producto(inventario, 1, 'Manzana', 0.50, 100)
agregar_producto(inventario, 2, 'Pera', 0.50, 100)

print('\nListado de productos:')
listar_productos(inventario)

# input("\nPresiona Enter para salir...")
