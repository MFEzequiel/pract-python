try:
    import os
    from pathlib import Path
except ImportError as e:
    print('Error al importar la libreria -->', e)

class Config:
  def __init__(self) -> None:
    self.cwd = os.getcwd()
    self.dir = os.path.join(self.cwd, 'project_worck', 'poo') 
  
class Manager:
  def __init__(self) -> None:
    pass

class Config:
  def __init__(self) -> None:
    pass