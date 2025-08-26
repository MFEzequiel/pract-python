# -*- coding: utf-8 -*-
try:
	from tkinter import Tk
	from ui import ui
except ImportError:
	print('Error al importar la libreria')

class Root():
	def __init__(self) -> None:
		self.root = Tk()
		
		self.root.title("Calculadora básica")
		# Evitar el redimensionamiento de una ventana de Tkinter
		self.root.resizable(0, 0)
		# Establecer un tamaño de ventana de Tkinter
		self.root.geometry("296x265")

		#UI
		self.ui = ui.UI(self.root)

	def run(self):
		self.root.mainloop()


root = Root()
# Inicialización de la root
root.run()