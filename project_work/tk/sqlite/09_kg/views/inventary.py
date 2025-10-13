try:
  from tkinter import Frame, Label, StringVar, Entry, Button, LabelFrame, Canvas, Scrollbar, ttk, messagebox, filedialog
except ImportError as e:
  print('Error al importar el módulo -->', e)

class Inventaries(Frame):
  def __init__(self, root=None) -> None:
    self.root = root
    self.widget()

  def widget(self):
    canvas_articles = LabelFrame(self.root, text='Articulos')

    self.canvas = Canvas(canvas_articles)
    self.scrollbar = Scrollbar(canvas_articles, orient='vertical', command=self.canvas.yview)
    self.scrollbar_frame = Frame(self.canvas)

    self.scrollbar_frame.bind(
      "<Configure>",
      lambda e: self.canvas.configure(
        scrollregion=self.canvas.bbox("all")
      )
    )

    self.canvas.create_window((0,0), window=self.scrollbar_frame, anchor='nw')
    self.canvas.config(yscrollcommand=self.scrollbar.set)
    
    #-----------search------------------
    search = LabelFrame(self.root, text='Buscar')
    self.combobox_search = ttk.Combobox(search)

    #-----------selects------------------
    select = LabelFrame(self.root, text='Seleción')
    self.label1 = Label(select, text='Articulo', wraplength=45)
    self.label2 = Label(select, text='Precio', wraplength=45)
    self.label3 = Label(select, text='Costo', wraplength=45)
    self.label4 = Label(select, text='Stock', wraplength=45)
    self.label5 = Label(select, text='Estado', wraplength=45)

    #-----------Buttons------------------
    bt = LabelFrame(self.root, text='Opciones')
    bt1 = Button(bt, text='Agregar')
    bt2 = Button(bt, text='Editar')
    bt3 = Button(bt, text='Eliminar')
    #-----------position widget------------------

    canvas_articles.place(x=300, y=10, width=700, height=581)
    self.canvas.pack(side='left', fill='both', expand=True)
    self.scrollbar.pack(side='right', fill='y')

    #-----------search------------------
    search.place(x=10, y=10, width=280, height=80)
    self.combobox_search.place(x=5, y=5, width=260, height=40)

    #-----------selects------------------
    select.place(x=10, y=95, width=280, height=190)
    self.label1.place(x=5, y=5)
    self.label2.place(x=5, y=40)
    self.label3.place(x=5, y=70)
    self.label4.place(x=5, y=100)
    self.label5.place(x=5, y=130)

    #-----------Buttons------------------
    bt.place(x=10, y=290, width=280, height=300)
    bt1.place(x=60, y=20, width=100, height=40)
    bt2.place(x=60, y=80, width=100, height=40)
    bt3.place(x=60, y=140, width=100, height=40)
