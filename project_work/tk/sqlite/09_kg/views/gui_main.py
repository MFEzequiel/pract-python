try:
  from tkinter import Frame, ttk, Label
  from views import sale, client, inventary
except ImportError as e:
  print('Error al importar el módulo -->', e)

class GUI(Frame):
  def __init__(self, root=None, conn=None, cursor=None) -> None:
    self.pather_tab = ttk.Notebook(root)
    self.cr = cursor

    tab_sales = self.create_tab(self.pather_tab, "sales", "Ventas", sale.Sale)
    tab_inventaries = self.create_tab(self.pather_tab, "sales", "Inventario", inventary.Inventaries)
    tab_clients = self.create_tab(self.pather_tab, "clients", "Clientes", client.Clients)

  def create_tab_db(self):
    tab_dbs = self.cr.execute('SELECT name FROM sqlite_master WHERE type="table"').fetchall()

    for tab_db in tab_dbs:
      options = tab_db[0]
      if options == 'sqlite_sequence':
        continue
      self.create_tab(self.pather_tab, options)

  def create_tab(self, pather, option, name, func=None):
    options = 'tab_' + option
    options = Frame(pather)
    pather.add(options, text=name)
    pather.pack(expand=1, fill="both")
    func(options)