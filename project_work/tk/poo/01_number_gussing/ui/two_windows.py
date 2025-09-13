try:
  from tkinter import Frame, Toplevel, Entry, Label, Button, CENTER, StringVar
  from core import game_logic, config
  from ui import main_window
except ImportError as e:
  print('Error al importar las libreria -->', e)

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

    self.text_low = StringVar()
    self.text_high = StringVar()

    #Entry
    self.entry_low = Entry(self.root, textvariable=self.text_low) 
    self.entry_high = Entry(self.root, textvariable=self.text_high)

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

    config.low = low
    config.high = high

    main_window.UI.update_text()
    self.root.destroy()