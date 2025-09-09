import tkinter as tk
from tkinter import filedialog 
from PIL import Image, ImageTk

def openimg():
    ruta = filedialog.askopenfilename()
    if ruta:
        img = Image.open(ruta) # abre la img con PIL
        img = ImageTk.PhotoImage(img) # combertirla img a un formato compatible con tk
        lb_img.config(image=img) # muestra la img en un label
        lb_img.image = img # gurda una referecia paraq no se pierda

root = tk.Tk()


btc = tk.Button(root, text='cargar', command=openimg)
btc.pack()

lb_img = tk.Label(root)
lb_img.pack()

root.mainloop()