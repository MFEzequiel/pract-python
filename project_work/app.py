from tkinter import Tk, Menu

root = Tk()
root.minsize(350, 350)  # valores numéricos sin comillas

bm = Menu(root)         # menú principal
root.config(menu=bm)

op_m = Menu(bm, tearoff=0)  # submenú "Archivo"
op_m.add_command(label='Nuevo')  # ítem dentro del submenú

bm.add_cascade(label='Archivo', menu=op_m)  # agregar el submenú al menú principal

root.mainloop()
