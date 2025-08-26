try:
  import random
except ImportError:
  print('Error al importar las librerias')

class GameLogic():
  def __init__(self, low, high) -> None:
    self.low = low
    self.high = high

    # como puedo hacerder al method input_data, sin tener q acceder al GameLogic, ya q este requiere de parametros

    #Intentos
    self.ch = 7
    #Intentos usados
    self.gc = 0

    self.random_number = random.randint(low, high)
  
  def input_data(self, number):
    while self.gc < self.ch:

      if (number > self.random_number):
        print(f'{number}, es mayor')
      elif (number < self.random_number):
        print(f'{number}, es menor')
      else:
        print('Adivinaste el número')