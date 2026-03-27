try:
  from tkinter import messagebox, Listbox, Button, Label, END
  from controllers import ctrl_cart
except ImportError as e:
  print('Error al importar el modulo -->', e)

class Interfaz:
  def __init__(self, root=None, controlador=None):
    # self.controlador = ctrl_cart.Controlador(self) if controlador is None else controlador
    self.controlador = controlador
    self.root = root
    self.root.title("Tienda Online")

    self.lista = Listbox(root) # Lista para mostrar articulos
    self.lista.pack()

    self.boton_agregar = Button(root, text="Agregar Artículo", command=self.agregar_articulo) # Boton para agregar articulo
    self.boton_agregar.pack()

    self.boton_eliminar = Button(root, text="Eliminar Artículo", command=self.eliminar_articulo) # Boton para eliminar articulo
    self.boton_eliminar.pack()

    self.boton_cupon = Button(root, text="Aplicar Cupón", command=self.aplicar_cupon) # Boton para aplicar cupon
    self.boton_cupon.pack()

    self.boton_finalizar = Button(root, text="Finalizar Compra", command=self.finalizar_compra) # Boton para finalizar compra
    self.boton_finalizar.pack()

    self.label_total = Label(root, text="Total: $0") # Etiqueta para mostrar total
    self.label_total.pack()

  def actualizar_carrito(self, articulos):
    self.lista.delete(0, END) # Limpiar lista actual
    for articulo in articulos: 
      self.lista.insert(END, f"{articulo['nombre']} - ${articulo['precio']}") # Actualizar lista de articulos

  def mostrar_total(self, total):
    self.label_total.config(text=f"Total: ${total:.2f}") # Actualizar etiqueta de total

  def agregar_articulo(self):
    self.controlador.add_article("ProductoX", 10.0) # Agregar articulo de ejemplo

  def eliminar_articulo(self):
    seleccion = self.lista.curselection() # Obtener seleccion actual
    if seleccion:
      item = self.lista.get(seleccion[0]) # Obtener articulo seleccionado
      nombre = item.split(' - ')[0] # Obtener nombre del articulo
      self.controlador.eliminar_articulo(nombre) # Eliminar articulo seleccionado

  def aplicar_cupon(self):
    self.controlador.aplicar_cupon(10)  # 10% de descuento

  def finalizar_compra(self):
    total = self.controlador.finalizar_compra() # Finalizar compra
    # print('\Views total: ', total, '\n') # Debug: imprimir total en consola
    messagebox.showinfo("Compra Finalizada", f"Total pagado: ${total}") # Mostrar mensaje de compra finalizada