try:
  from gui.main_window import launch_main_window
except ImportError as e:
  print('Error al importar la libreria -->', e)

if __name__ == "__main__":
  launch_main_window()