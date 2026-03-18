try:
  import pygame as pg
  import os
  from utils import config as c
  from enemy import Enemy, EnemyRunner
  from turret import Turret
except ImportError as e:
  print('Error al importar la libreria -->', e)

class RootGame:
  def __init__(self) -> None:
    self.pg = pg.init()

    self.screen = pg.display.set_mode((c.sd + c.size_panel, c.sh))
    pg.display.set_caption('Tower defents')
    self.clock = pg.time.Clock()
    self.runner = True

    self.path_files()
    self.load_image()
    self.create_group()
    self.create_enemies()
    self.draw_weapoint()

  def path_files(self):
    cwd = os.getcwd()
    self.path = os.path.join(cwd, 'project_work/pygame/00_g')

  def load_image(self):
    self.enemy_one_image = pg.image.load(os.path.join(self.path, 'assets/enemies/enemy_1.png')).convert_alpha()
    self.turret_image = pg.image.load(os.path.join(self.path, 'assets/enemies/enemy_1.png')).convert_alpha()

  def create_group(self):
    self.enemy_group = pg.sprite.Group()
    self.turret_group = pg.sprite.Group()

  def create_enemies(self):
    self.enemy_one = Enemy((300, 300), self.enemy_one_image)
    self.enemy_group.add(self.enemy_one)

  def create_turret(self, mouse_pos):
    mouse_tile_x = mouse_pos[0] // c.tile_size
    mouse_tile_y = mouse_pos[1] // c.tile_size
    turret = Turret(mouse_pos, self.turret_image, mouse_tile_x, mouse_tile_y)
    self.turret_group.add(turret)

  def draw_weapoint(self):
    # puntos del camino
    waypoints = [
      (100, 100),
      (400, 200),
      (400, 100),
      (200, 300)
    ]

  def run(self):
    while self.runner:
      self.clock.tick(c.fps)
      self.screen.fill('gray100')

      self.enemy_group.update()
      self.enemy_group.draw(self.screen)
      self.turret_group.draw(self.screen)
      
      # event hanfle
      for event in pg.event.get():
        if event.type == pg.QUIT:
          self.runner = False
        
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
          mouse_pos = pg.mouse.get_pos()
          # Check if mouse is on the game area
          if mouse_pos[0] < c.sd and mouse_pos[1] < c.sh:
            self.create_turret(mouse_pos)
      # update window
      pg.display.flip()

    pg.quit()

root = RootGame()
root.run()