import pygame as pg

# plantila eney
class Enemy(pg.sprite.Sprite): # Herencia (Herada sprite de pygame)
  def __init__(self, pos, image):
    pg.sprite.Sprite.__init__(self)
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.center = pos

  def update(self): # method (método)
    self.move()

  def move(self):
    self.rect.x += 1

class EnemyRunner(Enemy): # Hereda los atributos y metodos de la clase Enemyes
  def __init__(self, pos, image):
    super().__init__(pos, image)

  def move(self):
    self.rect.x += 5