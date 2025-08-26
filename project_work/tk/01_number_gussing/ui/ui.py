try:
  from tkinter import Frame, Label, Button, StringVar, Entry, CENTER
  from command import game_logic
except ImportError:
  print('Error al importar las librerias')

class UI(Frame):
  def __init__(self, root) -> None:
    super().__init__(root)
    self.data = game_logic
    print(self.data)
    
    # Elements
    self.label_welcome = Label(root, text='Tienes 7 oportunidades para adivinar el número entre {self.data.low} y {self.data.high}. ¡Comencemos!', wraplength=200, justify=CENTER)
    
    self.label_number = Label(root, text='Ingrese un número')
    self.box_number = StringVar()
    self.entry_number = Entry(root, textvariable=self.box_number)

    # buttons
    self.bt1 = Button(root, text='Agregar', command=lambda: self.data.)

    # Positions to elements
    self.label_welcome.grid(column=0, row=0, sticky='nsew')
    self.label_number.grid(column=0, row=1)

    self.entry_number.grid(column=1, row=1)

    self.bt1.grid(column=1, row=2, columnspan=2)