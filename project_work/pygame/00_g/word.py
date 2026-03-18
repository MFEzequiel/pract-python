from tkinter import Tk, ttk
import random

class Root:
  def __init__(self) -> None:
    self.root = Tk()
    self.root.title('Busca Mina')

    self.colums = 10
    self.rows = 20
    self.mine = 10
    self.buttons = []
    self.game_over = False

    self.create_tablero()

  def create_tablero(self):
    # self.tablero = [[0 for _ in range(self.colums)] for _ in range(self.rows)]
    for r in range(self.rows):
      files = []
      for col in range(self.colums):
        bt = ttk.Button(self.root, text='x', width=2, command=lambda r=r, col=col: self.click(r, col))
        bt.grid(row=r, column=col)
        files.append(bt)
      self.buttons.append(files)
    self.colocar_mina()

  def colocar_mina(self):
    colocar_mina = 0
    while colocar_mina < self.mine:
      r = random.randint(0 , self.rows -1)
      col = random.randint(0 , self.colums -1)
      if self.buttons[r][col]['text'] != 'M':
        self.buttons[r][col]['text'] = 'M'
        colocar_mina +=1

  def click(self, r, c):
    if self.game_over:
      return

    if self.buttons[r][c]['text'] == 'M':
      self.buttons[r][c]['bg'] = 'red'

  def run(self):
    self.root.mainloop()


root = Root()
root.run()