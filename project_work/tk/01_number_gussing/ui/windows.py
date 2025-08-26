try:
  from tkinter import Frame, Toplevel, Entry, Label, Button, CENTER
  from command.game_logic import GameLogic
except ImportError:
  print('Error al importar las librerias')

class WindowExtra(Frame):
  def __init__(self, root):
    super().__init__(root)

    self.root = Toplevel(root)
    # config root
    self.root.title('Adivina el número')
    self.root.minsize('350', '350')

    self.label_welcome = Label(self.root, text="¡Hola! Bienvenido al juego de adivina el número. Tienes 7 intentos para adivinar el número. ¡Comencemos!", wraplength=200, justify=CENTER)
    self.label_low = Label(self.root, text='Minimo')
    self.label_high = Label(self.root, text='Maximo')

    #Entry
    self.entry_low = Entry(self.root) 
    self.entry_high = Entry(self.root)

    # buttons
    self.bt1 = Button(self.root, text='Agregar', command=self.save_data)

    # Positions to elements
    self.label_welcome.grid(column=0, row=0, columnspan=2, pady=10)
    self.label_low.grid(column=0, row=1)
    self.label_high.grid(column=0, row=2)

    self.entry_low.grid(column=1, row=1)
    self.entry_high.grid(column=1, row=2)
    self.bt1.grid(column=0, row=3, columnspan=2)

  def save_data(self):
    low = int(self.entry_low.get())
    high = int(self.entry_high.get())

    game = GameLogic(low, high) 
    self.root.destroy()