import sqlite3
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from datetime import datetime
import os
from pathlib import Path

directory_tickets = 'tickets'
name_ticket = 'comprobante_venta.pdf'
name_ticket_mini = 'ticket.pdf'
name_ticket_dinamic = 'ticket_dinamico.pdf'

name_ticket = str(Path(name_ticket).with_suffix('.pdf').stem + '.pdf')
name_ticket_mini = str(Path(name_ticket_mini).with_suffix('.pdf').stem + '.pdf')
name_ticket_dinamic = str(Path(name_ticket_dinamic).with_suffix('.pdf').stem + '.pdf')

full_path_tikets = os.path.join(directory_tickets, name_ticket)
full_path_tikets_mini = os.path.join(directory_tickets, name_ticket_mini)
full_path_tikets_dinamic = os.path.join(directory_tickets, name_ticket_dinamic)
if not os.path.exists(directory_tickets):
  os.makedirs(directory_tickets)


# Crear y conectar a la base de datos SQLite
conn = sqlite3.connect('ventas.db')
cursor = conn.cursor()

# Crear tabla cliente
cursor.execute('''
CREATE TABLE IF NOT EXISTS cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
)
''')

# Crear tabla producto
cursor.execute('''
CREATE TABLE IF NOT EXISTS producto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL
)
''')

# Insertar datos de ejemplo
cursor.execute("INSERT INTO cliente (nombre) VALUES ('Juan Pérez')")
cursor.execute("INSERT INTO producto (nombre, precio) VALUES ('Laptop', 1200.00)")
cursor.execute("INSERT INTO producto (nombre, precio) VALUES ('Mouse', 25.50)")
conn.commit()


# Función para crear el comprobante de venta en PDF
def crear_comprobante_venta(id_cliente: int, productos_comprados: list[int], archivo_salida='comprobante.pdf'):
    # Obtener cliente
    cursor.execute("SELECT nombre FROM cliente WHERE id = ?", (id_cliente,))
    cliente = cursor.fetchone()
    if not cliente:
        print("Cliente no encontrado")
        return
    nombre_cliente = cliente[0]

    # Obtener detalles de productos
    productos = []
    total = 0.0
    for id_producto in productos_comprados:
        cursor.execute("SELECT nombre, precio FROM producto WHERE id = ?", (id_producto,))
        result = cursor.fetchone()
        if result:
            nombre_producto, precio = result
            productos.append((nombre_producto, precio))
            total += precio

    # Crear PDF
    c = canvas.Canvas(archivo_salida, pagesize=letter)
    width, height = letter

    y = height - 50
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Comprobante de Venta")
    c.setFont("Helvetica", 12)
    y -= 30
    c.drawString(50, y, f"Cliente: {nombre_cliente}")
    y -= 20
    c.drawString(50, y, f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    y -= 30

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Productos:")
    y -= 20
    c.setFont("Helvetica", 12)

    for nombre_producto, precio in productos:
        c.drawString(60, y, f"{nombre_producto} - ${precio:.2f}")
        y -= 20

    y -= 10
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, f"Total: ${total:.2f}")

    c.save()
    print(f"Comprobante guardado como: {archivo_salida}")

def crear_ticket_pequeno(id_cliente: int, productos_comprados: list[int], archivo_salida='ticket.pdf'):
    # Obtener cliente
    cursor.execute("SELECT nombre FROM cliente WHERE id = ?", (id_cliente,))
    cliente = cursor.fetchone()
    if not cliente:
        print("Cliente no encontrado")
        return
    nombre_cliente = cliente[0]

    # Obtener detalles de productos
    productos = []
    total = 0.0
    for id_producto in productos_comprados:
        cursor.execute("SELECT nombre, precio FROM producto WHERE id = ?", (id_producto,))
        result = cursor.fetchone()
        if result:
            nombre_producto, precio = result
            productos.append((nombre_producto, precio))
            total += precio

    # Tamaño del ticket: 80mm de ancho, altura calculada
    width = 80 * mm  # 80 mm
    line_height = 15
    padding = 20
    num_lines = 6 + len(productos)  # cabecera + productos + total
    height = num_lines * line_height + padding

    c = canvas.Canvas(archivo_salida, pagesize=(width, height))

    y = height - 20
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(width / 2, y, "TICKET DE VENTA")
    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(10, y, f"Cliente: {nombre_cliente}")
    y -= 14
    c.drawString(10, y, f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    y -= 20

    c.setFont("Helvetica-Bold", 10)
    c.drawString(10, y, "Productos:")
    y -= 14
    c.setFont("Helvetica", 10)

    for nombre_producto, precio in productos:
        texto = f"{nombre_producto[:20]:<20} ${precio:.2f}"
        c.drawString(10, y, texto)
        y -= 14

    y -= 10
    c.setFont("Helvetica-Bold", 11)
    c.drawString(10, y, f"Total: ${total:.2f}")
    c.save()

    print(f"Ticket pequeño guardado como: {archivo_salida}")

def crear_ticket_dinamico(id_cliente: int, productos_comprados: list[int], archivo_salida='ticket_dinamico.pdf'):
    # Obtener cliente
    cursor.execute("SELECT nombre FROM cliente WHERE id = ?", (id_cliente,))
    cliente = cursor.fetchone()
    if not cliente:
        print("Cliente no encontrado")
        return
    nombre_cliente = cliente[0]

    # Obtener productos y calcular total
    productos = []
    total = 0.0
    for id_producto in productos_comprados:
        cursor.execute("SELECT nombre, precio FROM producto WHERE id = ?", (id_producto,))
        result = cursor.fetchone()
        if result:
            nombre_producto, precio = result
            productos.append((nombre_producto, precio))
            total += precio

    # Medidas para ticket pequeño
    width = 80 * mm  # 80 mm de ancho
    line_height = 14
    header_height = 60
    footer_height = 40
    product_lines = len(productos)
    height = header_height + footer_height + (product_lines * line_height)

    c = canvas.Canvas(archivo_salida, pagesize=(width, height))

    y = height - 20
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(width / 2, y, "TICKET DE VENTA")

    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(10, y, f"Cliente: {nombre_cliente}")
    y -= 14
    c.drawString(10, y, f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    y -= 20

    c.setFont("Helvetica-Bold", 10)
    c.drawString(10, y, "Productos:")
    y -= 14
    c.setFont("Helvetica", 10)

    for nombre_producto, precio in productos:
        texto = f"{nombre_producto[:20]:<20} ${precio:.2f}"
        c.drawString(10, y, texto)
        y -= line_height

    y -= 5
    c.setFont("Helvetica-Bold", 11)
    c.drawString(10, y, f"Total: ${total:.2f}")

    y -= 20
    c.setFont("Helvetica-Oblique", 9)
    c.drawCentredString(width / 2, y, "¡Gracias por su compra!")

    c.save()
    print(f"Ticket dinámico generado: {archivo_salida}")


# Ejemplo de uso
if __name__ == '__main__':
    crear_comprobante_venta(id_cliente=1, productos_comprados=[1, 2], archivo_salida=full_path_tikets)
    crear_ticket_pequeno(id_cliente=1, productos_comprados=[1, 2], archivo_salida=full_path_tikets_mini)
    crear_ticket_dinamico(id_cliente=1, productos_comprados=[1, 2, 1, 2, 1, 2, 1, 2], archivo_salida=full_path_tikets_dinamic)
    conn.close()