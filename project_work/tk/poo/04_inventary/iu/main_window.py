try:
  import tkinter as tk
  from tkinter import messagebox
  from core import config
  from logic import inventory
except ImportError as e:
  print('Error al importar la libreria -->', e)

def launch_main_window():
  root = tk.Tk()
  root.title(config.APP_TITLE)
  root.geometry(config.APP_GEOMETRY)

  # Labels y Entradas
  tk.Label(root, text="ID").grid(row=0, column=0)
  tk.Label(root, text="Nombre").grid(row=1, column=0)
  tk.Label(root, text="Precio").grid(row=2, column=0)
  tk.Label(root, text="Stock").grid(row=3, column=0)

  entry_id = tk.Entry(root)
  entry_nombre = tk.Entry(root)
  entry_precio = tk.Entry(root)
  entry_stock = tk.Entry(root)

  entry_id.grid(row=0, column=1)
  entry_nombre.grid(row=1, column=1)
  entry_precio.grid(row=2, column=1)
  entry_stock.grid(row=3, column=1)

  # Funciones para botones
  def agregar():
    try:
      id = int(entry_id.get())
      nombre = entry_nombre.get()
      precio = float(entry_precio.get())
      stock = int(entry_stock.get())
      msg = inventory.agregar_producto(config.inventario, id, nombre, precio, stock)
      messagebox.showinfo("Resultado", msg)
      listar()
    except ValueError:
      messagebox.showerror("Error", "Datos inválidos.")

  def eliminar():
    try:
      id = int(entry_id.get())
      msg = inventory.eliminar_producto(config.inventario, id)
      messagebox.showinfo("Resultado", msg)
      listar()
    except ValueError:
      messagebox.showerror("Error", "ID inválido.")

  def actualizar():
      try:
      id = int(entry_id.get())
      nombre = entry_nombre.get() or None
      precio = float(entry_precio.get()) if entry_precio.get() else None
      stock = int(entry_stock.get()) if entry_stock.get() else None
      msg = inventory.actualizar_producto(config.inventario, id, nombre, precio, stock)
      messagebox.showinfo("Resultado", msg)
      listar()
    except ValueError:
      messagebox.showerror("Error", "Datos inválidos.")

  def listar():
    lista.delete(0, tk.END)
    productos = inventory.listar_productos(config.inventario)
    for producto in productos:
      lista.insert(tk.END, producto)

  # Botones
  tk.Button(root, text="Agregar", command=agregar).grid(row=4, column=0)
  tk.Button(root, text="Eliminar", command=eliminar).grid(row=4, column=1)
  tk.Button(root, text="Actualizar", command=actualizar).grid(row=4, column=2)
  tk.Button(root, text="Listar", command=listar).grid(row=5, column=1)

  # Lista de productos
  lista = tk.Listbox(root, width=60)
  lista.grid(row=6, column=0, columnspan=3, pady=10)

  root.mainloop()