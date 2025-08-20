try:
  import random
except ImportError:
  print('Error al importar las librerias')

class GameLogic():
  def __init__(self, number, low, high) -> None:
    self.number = number
    self.low = low
    self.high = high

    self.ch = 7
    self.gc = 0

    # while self.gc < self.ch:
    #   pass
  
  def input_data(self, low, high):
    self.dic = {
      "low": low,
      "high": high
    }
    return self.dic