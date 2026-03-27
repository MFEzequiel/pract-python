from tkinter import Tk, ttk
import random

class Root:
  def __init__(self) -> None:
    self.root = Tk()
    self.root.title('Busca Mina')
    
    # config board
    self.columns = 10
    self.rows = 10
    self.mine = 10
    self.buttons = []
    self.finish_game = False
    # call methods
    self.create_table()

  def create_table(self):
    for r in range(self.rows):
      files = []
      for c in range(self.columns):
        bt = ttk.Button(self.root, text='', width=2, command=lambda r=r, c=c: self.click(r, c))
        bt.grid(row=r, column=c) 
        files.append(bt)
      self.buttons.append(files)
    self.add_mine()

  def add_mine(self):
    add_mine = 0

    while add_mine < self.mine:
      r = random.randint(0, self.rows - 1)
      c = random.randint(0, self.columns - 1)

      if self.buttons[r][c]['text'] != 'M':
        self.buttons[r][c]['text'] = 'M'
        add_mine += 1

  def click(self, r, c):
    if self.finish_game:
      return

    if self.buttons[r][c]['text'] == 'M':
      self.buttons[r][c]['text'] = 'E'
      self.game_over()
    else:
      self.revel()

  def revel(self):
    pass

  def game_over(self):
    pass
      
  def run(self):
    self.root.mainloop()
  

root = Root()
root.run()