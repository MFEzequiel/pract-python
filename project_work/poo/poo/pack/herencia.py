class Celular():
  def __init__(self, model, marca, camera, read_camera, front_camera) -> None:
    self.model = model
    self.marca = marca
    self.camera = camera
    self.read_camera = read_camera
    self.front_camera = front_camera

class Smartphone(Celular):
  def __init__(self, model, marca, camera, read_camera, front_camera, gps, bluetooth) -> None:
    super().__init__(model, marca, camera, read_camera, front_camera)
    self.gps = gps
    self.bluetooth = bluetooth

celular1 = Smartphone('s23', 'samsung', '48MP', '38MP', "24PM", True, True)