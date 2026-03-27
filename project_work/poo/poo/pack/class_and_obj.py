# static
class Celular():
  celular1_marca = 'samsung'
  celular1_camaraT = '48MP'
  celular1_camaraF = '24MP'

class DCelular():
  def __init__(self, camera, read_camera, front_camera) -> None:
    self.camera = camera
    self.read_camera = read_camera
    self.front_camera = front_camera