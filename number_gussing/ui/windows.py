try:
  from tkinter import ttk, Toplevel, CENTER
except ImportError:
  print('Error al importar las librerias')

class WindowExtra():
  def __init__(self, root) -> None:
    self.root = Toplevel(root)

    # config root
    self.root.title('Adivina el número')
    self.root.minsize('350', '350')

    self.label_welcome = ttk.Label(root, text="¡Hola! Bienvenido al juego de adivina el número. Tienes 7 intentos para adivinar el número. ¡Comencemos!", wraplength=200, justify=CENTER)
    self.label_low = ttk.Label()
    self.label_high = ttk.Label()
        

    # buttons
    self.bt1 = ttk.Button(root, text='Agregar')

    # Positions to elements
    self.label_welcome.grid(column=0, row=0, sticky='nsew')
