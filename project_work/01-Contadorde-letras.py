from tkinter import *

# Crear la ventana, título e icono de la calculadora
root = Tk()
root.title("Calculadora básica")
# root.iconbitmap("img/calculator.ico")
# Evitar el redimensionamiento de una ventana de Tkinter
root.resizable(0, 0)
# Establecer un tamaño de ventana de Tkinter
root.geometry("296x265")

# Crear la pantalla de la calculadora

pantalla = Entry(root,
				width=22,
				bg="black",
				fg="white",
				borderwidth=0,
				font=('arial', 18, 'bold'))

pantalla.grid(row=0, padx=2, pady=2, columnspan=4)

# Añadir los botones de la calculadora de Tkinter
boton_1 = Button(root,text="1",width=9,height=3,bg="white",fg="red",borderwidth=0,cursor="hand2").grid(row=1, column=0, padx=1, pady=1)

boton_2 = Button(root,text="2",width=9,height=3,bg="white",fg="red",borderwidth=0,cursor="hand2").grid(row=1, column=1, padx=1, pady=1)

boton_3 = Button(root,text="3",width=9,height=3,bg="white",fg="red",borderwidth=0,cursor="hand2").grid(row=1, column=2, padx=1, pady=1)

boton_4 = Button(root,text="4",
				width=9,
				height=3,
				bg="white",
				fg="red",
				borderwidth=0,
				cursor="hand2").grid(row=2, column=0, padx=1, pady=1)

boton_5 = Button(root,text="5",
				width=9,
				height=3,
				bg="white",
				fg="red",
				borderwidth=0,
				cursor="hand2").grid(row=2, column=1, padx=1, pady=1)

boton_6 = Button(root,text="6",
				width=9,
				height=3,
				bg="white",
				fg="red",
				borderwidth=0,
				cursor="hand2").grid(row=2, column=2, padx=1, pady=1)

boton_7 = Button(root,text="7",
				width=9,
				height=3,
				bg="white",
				fg="red",
				borderwidth=0,
				cursor="hand2").grid(row=3, column=0, padx=1, pady=1)

boton_8 = Button(root,text="8",
				width=9,
				height=3,
				bg="white",
				fg="red",
				borderwidth=0,
				cursor="hand2").grid(row=3, column=1, padx=1, pady=1)

boton_9 = Button(root,text="9",
				width=9,
				height=3,
				bg="white",
				fg="red",
				borderwidth=0,
				cursor="hand2").grid(row=3, column=2, padx=1, pady=1)


boton_igual = Button(root,text="=",
				width=20,
				height=3,
				bg="red",
				fg="white",
				borderwidth=0,
				cursor="hand2").grid(row=4, column=0, columnspan=2, padx=1, pady=1)

boton_punto = Button(root,text=".",
				width=9,
				height=3,
				bg="spring green",
				fg="black",
				cursor="hand2",
				borderwidth=0).grid(row=4, column=2, padx=1, pady=1)

boton_mas = Button(root,text="+",
				width=9,
				height=3,
				bg="deep sky blue",
				fg="black",
				borderwidth=0,
				cursor="hand2").grid(row=1, column=3, padx=1, pady=1)

boton_menos = Button(root,text="-",
				width=9,
				height=3,
				bg="deep sky blue",
				fg="black",
				borderwidth=0,
				cursor="hand2").grid(row=2, column=3, padx=1, pady=1)

boton_multiplicacion = Button(root,text="*",width=9,height=3,bg="deep sky blue",fg="black",borderwidth=0,cursor="hand2").grid(row=3, column=3, padx=1, pady=1)

boton_division = Button(root,text="/",width=9,height=3,bg="deep sky blue",fg="black",borderwidth=0,cursor="hand2").grid(row=4, column=3, padx=1, pady=1)

# Inicialización de la root
root.mainloop()