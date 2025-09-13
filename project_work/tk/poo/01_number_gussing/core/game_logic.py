try:
  import random
  from core import config
except ImportError as e:
  print('Error al importar las libreria', e)

class GameLogic():
  def __init__(self) -> None:
    # como puedo hacerder al method input_data, sin tener q acceder al GameLogic, ya q este requiere de parametros

    #Intentos
    self.ch = 7
    #Intentos usados
    self.gc = 0

    self.random_number = random.randint(config.low, config.high)
  
  def input_number(self, number):
    while self.gc < self.ch:

      if (number > self.random_number):
        print(f'{number}, es mayor')
      elif (number < self.random_number):
        print(f'{number}, es menor')
      else:
        print('Adivinaste el número')