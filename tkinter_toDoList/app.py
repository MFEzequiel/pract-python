import tkinter as tk
from ui import ui

class Root():
  def __init__(self) -> None:
    self.root = tk.Tk()

  def run(self):
    self.root.mainloop()
    # configure root

    # call class ui
    self.ui = ui.UI(root)
     

root = Root()
root.run()