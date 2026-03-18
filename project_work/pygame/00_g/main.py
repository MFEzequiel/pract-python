try:
  import pygame as pg
  from utils import config as c
  from word import Word
  from enemy import Enemy, EnemyRunner
except ImportError as e:
  print('Error al importar la libreria -->', e)

# iniciar pygame
pg.init()

# create window
screen = pg.display.set_mode((c.sd, c.sh))
pg.display.set_caption('Tower defents')

clock = pg.time.Clock()

# load image
# map
map_word = pg.image.load('asset/level/word_1.png').convert_alpha()
# enemies
enemy_one_image = pg.image.load('asset/enemies/enemy_1.png').convert_alpha()
enemy_zr_image = pg.image.load('asset/enemies/enemy_2.png').convert_alpha()

# create word
word = Word(map_word)

# create group
enemy_group = pg.sprite.group()

# create enemies
enemy_one = Enemy((300, 300), enemy_one_image)
enemy_runner = EnemyRunner((300, 300), enemy_zr_image)
# agregar enemies in grupo enemy
enemy_group.add(enemy_one)

# puntos del camino
waypoints = [
  (100, 100),
  (400, 200),
  (400, 100),
  (200, 300)
]

# game loop
run = True 
while run:
  # event hanfle
  for event in pg.event.get():
    if event.type == pg.QUIT:
      run = False

  clock.tick(c.fps)
  # draw word
  word.draw(screen)
  # actualizar grupo enemigo
  enemy_group.update()

  # grupo de dibugo agrega a la ventana
  enemy_group.draw(screen)

  # update window
  pg.display.filp()

pg.quit()