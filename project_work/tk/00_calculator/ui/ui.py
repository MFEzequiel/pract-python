try:
  from tkinter import Frame, Entry, Button
  from command.logic import Logic
except ImportError:
  print('Error al importar la libreria')

class UI(Frame):
  def __init__(self, root):
    super().__init__(root)

		# Crear la ventana, título e icono de la calculadora
    # Crear la pantalla de la calculadora
    self.root2 = Entry(root, width=22, bg="black", fg="white", borderwidth=0, font=('arial', 18, 'bold')).grid(row=0, padx=2, pady=2, columnspan=4)

    # # Añadir los botones de la calculadora de Tkinter
    self.btn_1 = Button(root, text="0", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: Logic.inserValue('0')).grid(row=6, column=0, padx=1, pady=1)
    self.btn_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: Logic.inserValue('1')).grid(row=1, column=0, padx=1, pady=1)
    self.btn_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: Logic.inserValue('2')).grid(row=1, column=1, padx=1, pady=1)
    self.btn_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: Logic.inserValue('3')).grid(row=1, column=2, padx=1, pady=1)
    self.btn_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: Logic.inserValue('4')).grid(row=2, column=0, padx=1, pady=1)
    self.btn_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: Logic.inserValue('5')).grid(row=2, column=1, padx=1, pady=1)
    self.btn_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: Logic.inserValue('6')).grid(row=2, column=2, padx=1, pady=1)
    self.btn_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: Logic.inserValue('7')).grid(row=3, column=0, padx=1, pady=1)
    self.btn_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: Logic.inserValue('8')).grid(row=3, column=1, padx=1, pady=1)
    self.btn_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: Logic.inserValue('9')).grid(row=3, column=2, padx=1, pady=1)

    self.btn_igual = Button(root,text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor="hand2").grid(row=4, column=0, columnspan=2, padx=1, pady=1)
    self.btn_punto = Button(root,text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0).grid(row=4, column=2, padx=1, pady=1)
    self.btn_mas = Button(root,text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=1, column=3, padx=1, pady=1)
    self.btn_menos = Button(root,text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=2, column=3, padx=1, pady=1)
    self.btn_multiplicacion = Button(root,text="*",width=9,height=3,bg="deep sky blue",fg="black",borderwidth=0,cursor="hand2").grid(row=3, column=3, padx=1, pady=1)
    self.btn_division = Button(root,text="/",width=9,height=3,bg="deep sky blue",fg="black",borderwidth=0,cursor="hand2").grid(row=4, column=3, padx=1, pady=1)
