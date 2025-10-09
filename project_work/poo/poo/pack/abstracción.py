try:
  from abc import ABC, abstractmethod
except ImportError as e:
  print('Error importando modulos: ', e)

class Celular(ABC):
  def __init__(self, model, marca, camera, read_camera, front_camera) -> None:
    self.model = model
    self.marca = marca
    self.camera = camera
    self.read_camera = read_camera
    self.front_camera = front_camera

  @abstractmethod
  def more_info(self):
    pass

class Smartphone(Celular):
  def __init__(self, model, marca, camera, read_camera, front_camera, gps, bluetooth) -> None:
    super().__init__(model, marca, camera, read_camera, front_camera)
    self.gps = gps
    self.bluetooth = bluetooth

  # Implementación obligatoria del métodod abstracto
  def more_info(self):
    return print(f'Model: {self.model},
      Marca: {self.marca},
      Camara: {self.camera},
      Camara Trasera: {self.read_camera},
      Camara Frontal: {self.front_camera},
      GPS: {self.gps},
      Bluetooth: {self.bluetooth}'
    )

celular1 = Smartphone('s23', 'samsung', '48MP', '38MP', "24PM", True, True)

class animal(ABC):
  def __init__(self, raza, edad, altura) -> None:
    self.raza = raza
    self.edad = edad
    self.altura = altura

  @abstractmethod
  def sound(self):
    pass

class dog(animal):
  def __init__(self, raza, edad, altura) -> None:
    super().__init__(raza, edad, altura)

  def sound(self):
    return print('Guau Guau')

class cat(animal):
  def __init__(self, raza, edad, altura) -> None:
    super().__init__(raza, edad, altura)

  def sound(self):
    return print('Miau Miau')