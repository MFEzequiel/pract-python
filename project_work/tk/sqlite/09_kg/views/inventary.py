try:
  from tkinter import Frame, Label, StringVar, Entry, Button, LabelFrame, Canvas, Scrollbar, ttk, messagebox, filedialog, Toplevel
  import config
  import os
  from PIL import Image, ImageTk
  from modules import model_db
  import sqlite3 as sql
except ImportError as e:
  print('Error al importar el módulo -->', e)

class Inventaries(Frame):
  def __init__(self, root=None) -> None:
    self.root = root
    self.img_dir = config.DIR_IMAGE
    self.model = model_db.DBModel()
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
    bt1 = Button(bt, text='Agregar', command=self.add_article)
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

  def load_image(self):
    file_path = filedialog.askopenfilename(
      initialdir=config.DIR_IMAGE,
      filetypes=[("Image files", "*.png *.jpg *.gif")]
    )

    if file_path:
      img = Image.open(file_path)
      img = img.resize((200, 200), Image.LANCZOS)

      img_name = os.path.basename(file_path)

      img_save_pach = os.path.join(self.img_dir, img_name)
      img.save(img_save_pach)

      self.img_tk = ImageTk.PhotoImage(img)

      self.product_img = self.img_tk
      file_path = img_save_pach

      img_lb = Label(self.frameimg, image=self.img_tk)
      img_lb.place(x=0, y=0, width=200, height=200)

  def add_article(self):
    top = Toplevel(self.root)
    top.title('Agregar Articulo')
    top.geometry('700x400+200+50')
    top.transient(self.root)
    top.grab_set()
    top.focus_set()
    top.lift()

    box_art = StringVar
    Label(top, text='Articulos: ').place(x=20, y=20, width=80, height=25)
    entry_art = Entry(top, textvariable=box_art)
    entry_art.place(x=120, y=20, width=250, height=30)

    box_price = StringVar
    Label(top, text='Precio: ').place(x=20, y=60, width=80, height=25)
    entry_price = Entry(top, textvariable=box_price)
    entry_price.place(x=120, y=60, width=250, height=30)

    box_costo = StringVar
    Label(top, text='Costo: ').place(x=20, y=100, width=80, height=25)
    entry_costo = Entry(top, textvariable=box_costo)
    entry_costo.place(x=120, y=100, width=250, height=30)

    box_stock = StringVar
    Label(top, text='Stock: ').place(x=20, y=140, width=80, height=25)
    entry_stock = Entry(top, textvariable=box_stock)
    entry_stock.place(x=120, y=140, width=250, height=30)
    
    box_state = StringVar
    Label(top, text='Estado: ').place(x=20, y=200, width=80, height=25)
    entry_state = Entry(top, textvariable=box_state)
    entry_state.place(x=120, y=200, width=250, height=30)

    self.frameimg = Frame(top, bg='#fff')
    self.frameimg.place(x=445, y=10, width=200, height=200)

    bt_img = Button(top, text='Cargar Imágen', command=self.load_image)
    bt_img.place(x=470, y=240, width=150, height=40)

    def save_data():
      art = entry_art.get()
      price = entry_price.get()
      costo = entry_costo.get()
      stock = entry_stock.get()
      state = entry_state.get()

      if not art or not price or not stock or not state:
        messagebox.showerror("Error", "Todo los campos deben ser completados ")
        return
      
      try:
        price = float(price)
        costo = float(costo)
        stock = int(stock)
      except ValueError as e:
        print("price, costo y stock")
        messagebox.showerror("Error", "price, costo y stock deben ser números validos")
        return

      if hasattr(self.root, "img_path"):
        img_path = self.img_path
      else:
        img_path = os.path.join(self.img_dir, 'default.png')
        
      try:
        with open(img_path, 'rb') as file:
          img_bytes = file.read()

        query = 'INSERT INTO products (name, price, costo, stock, state, image) VALUES (?, ?, ?, ?, ?, ?)'
        self.model.excecute(query, (art, price, costo, stock, state, img_bytes))
        
        messagebox.showinfo('Exito', 'Articulo agregado correctamente')
        top.destroy()
      except sql.Error as e:
        print("Error al cargar el articulo --> ", e)
        messagebox.showerror('Error', 'Error al agregar el articulo')

    bt_save = Button(top, text='Guardar Imágen', command=save_data)
    bt_save.place(x=20, y=280, width=150, height=40)
    bt_save = Button(top, text='Guardar Imágen', command=top.destroy)
    bt_save.place(x=20, y=340, width=150, height=40)