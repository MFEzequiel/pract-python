try:
  from tkinter import Tk
  from ui import menu
  from core import file_manager 
except ImportError as e:
  print("Error importing module: ", e)

class Root:
  def __init__(self):
    self.root = Tk()
    self.root.title("SQLite to Excel")
    self.root.geometry("400x200")
    self.root.resizable(0, 0)
    self.export_to_excel = file_manager.ClientExporte().create_excel()

    self.menu = menu.MenuApp(self.root, self.export_to_excel)

  def run(self):
    self.root.mainloop()

if __name__ == "__main__":
  app = Root()
  app.run()