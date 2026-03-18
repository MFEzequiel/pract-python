import random
import pygame as pg
from utils import config as c

class Turret(pg.sprite.Sprite):
  def __init__(self, pos=None, image=None, tile_x=None,  tile_y=None):
    pg.sprite.Sprite.__init__(self)
    self.tile_x = tile_x
    self.tile_y = tile_y
    # calculate center cordinates
    self.x = (self.tile_x + 0.5) * c.tile_size
    self.y = (self.tile_y + 0.5) * c.tile_size
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.center = (self.x, self.y)