try:
  import tkinter as tk
  from tkinter import messagebox
  from core import config
  from logic.roulette_engine import RouletteGame
except ImportError as e:
  print('Error al importar la libreria -->', e)

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Roulette Simulator")
        self.game = RouletteGame()
        self.setup_ui()

    def setup_ui(self):
        # Create buttons, labels, etc.
        pass
