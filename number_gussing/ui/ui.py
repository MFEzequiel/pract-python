try:
  from tkinter import ttk, Frame, CENTER
  from command import game_logic
except ImportError:
  print('Error al importar las librerias')

class UI(Frame):
  def __init__(self, root) -> None:
    super().__init__(root)
    self.data = game_logic.GameLogic(1, 2, 3)
    self.data1 = self.data.input_data(2,3)
    
    # Elements
    self.label_welcome = ttk.Label(root, text=f'Tienes 7 oportunidades para adivinar el número entre {self.data1["low"]} y {self.data1["high"]}. ¡Comencemos!', wraplength=200, justify=CENTER)
    
    self.label_number = ttk.Label()
    # buttons
    self.bt1 = ttk.Button(root, text='Agregar')

    # Positions to elements
    self.label_welcome.grid(column=0, row=0, sticky='nsew')