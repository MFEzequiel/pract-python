# --------------------------
# importar librerias
# --------------------------
import pygame
import random
import sys

# --------------------------
# CONFIGURACIÓN
# --------------------------
FPS = 30
TAM_CASILLA = 40
COLUMNAS = 10
FILAS = 10
MINAS = 10

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS = (160, 160, 160)
GRIS_OSCURO = (100, 100, 100)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
# --------------------------
# inicializar pygame
# --------------------------
pygame.init()
fuente = pygame.font.SysFont("arial", 22)

# --------------------------
# crear el tablero del juego
# --------------------------
def crear_tablero():
  tablero = [
    [0 for _ in range(COLUMNAS)]
    for _ in range(FILAS)
  ]
# --------------------------
# colocar minas
# --------------------------
  minas_colocadas = 0
  while minas_colocadas < MINAS:
    f = random.randint(0, FILAS - 1)
    c = random.randint(0, COLUMNAS - 1)
    if tablero[f][c] != -1:
      tablero[f][c] = -1
      minas_colocadas += 1
# --------------------------
# calcular números
# --------------------------
  for f in range(FILAS):
    for c in range(COLUMNAS):
      if tablero[f][c] == -1:
        continue
      contador = 0
      for df in (-1, 0, 1):
        for dc in (-1, 0, 1):
          nf, nc = f + df, c + dc
          if (0 <= nf < FILAS and 0 <= nc < COLUMNAS
            and tablero[nf][nc] == -1
          ):
            contador += 1
      tablero[f][c] = contador

  return tablero
# --------------------------
# mostrar la casilla al hacer click
# --------------------------
def revelar_casilla(revelado, tablero, f, c):
  if revelado[f][c]:
    return

  revelado[f][c] = True
# --------------------------
# si la casillla es 0, revelar vecinos
# --------------------------
  if tablero[f][c] == 0:
    for df in (-1, 0, 1):
      for dc in (-1, 0, 1):
        nf, nc = f + df, c + dc
        if 0 <= nf < FILAS and 0 <= nc < COLUMNAS:
          if not revelado[nf][nc]:
            revelar_casilla(revelado, tablero, nf, nc)
# --------------------------
# comprobar si el jugador gano o perdio
# --------------------------
def verificar_victoria(revelado, tablero):
  for f in range(FILAS):
    for c in range(COLUMNAS):
      if tablero[f][c] != -1 and not revelado[f][c]:
        return False
    return True

# --------------------------
# JUEGO PRINCIPAL
# --------------------------
def main():
  ventana = pygame.display.set_mode(
    (COLUMNAS * TAM_CASILLA, FILAS * TAM_CASILLA)
  )
  pygame.display.set_caption("Buscaminas")
  clock = pygame.time.Clock()

  tablero = crear_tablero()
  revelado = [
    [False] * COLUMNAS for _ in range(FILAS)
  ]
  banderas = [
    [False] * COLUMNAS for _ in range(FILAS)
  ]
  game_over = False
  victoria = False

  while True:
    clock.tick(FPS)

    for evento in pygame.event.get():
      if evento.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

      if (evento.type == pygame.MOUSEBUTTONDOWN
        and not game_over
      ):
        x, y = evento.pos
        c = x // TAM_CASILLA
        f = y // TAM_CASILLA

        if evento.button == 1:  # clic izquierdo
          if not banderas[f][c]:
            if tablero[f][c] == -1:
              game_over = True
            else:
              revelar_casilla(revelado, tablero, f, c)
              if verificar_victoria(revelado, tablero):
                game_over = True
                victoria = True
        elif evento.button == 3:  # clic derecho
          if not revelado[f][c]:
            banderas[f][c] = not banderas[f][c]

      # --------------------------
      # DIBUJAR TABLERO
      # --------------------------
      ventana.fill(GRIS_OSCURO)

      for f in range(FILAS):
        for c in range(COLUMNAS):
          rect = pygame.Rect(c*TAM_CASILLA, f*TAM_CASILLA, TAM_CASILLA,
            TAM_CASILLA
          )

          if revelado[f][c]:
            pygame.draw.rect(ventana, GRIS, rect)
            if tablero[f][c] > 0:
              texto = fuente.render(str(tablero[f][c]), True, AZUL)
              ventana.blit(texto, (c*TAM_CASILLA + 15, f*TAM_CASILLA + 8))
          else:
            pygame.draw.rect(ventana, GRIS_OSCURO, rect)
            if banderas[f][c]:
              pygame.draw.circle(ventana, ROJO, rect.center, 10)

          pygame.draw.rect(ventana, NEGRO, rect, 1)

          if game_over and tablero[f][c] == -1:
            pygame.draw.circle(ventana, NEGRO, rect.center, 10)

    # Mensaje final
    if game_over:
      msg = "¡Ganaste!" if victoria else "Game Over"
      texto = fuente.render(msg, True, BLANCO)
      ventana.blit(texto, (10, 10))

    pygame.display.update()

if __name__ == "__main__":
    main()