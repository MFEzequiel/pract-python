import tkinter as tk
from ui import ui

class Root():
  def __init__(self) -> None:
    self.root = tk.Tk()
    # configure root

    # call class ui
    self.ui = ui.UI(root)

  def run(self):
    self.root.mainloop()
     

root = Root()
root.run()