''
import tkinter as tk
from modulos.gui import UI, Barra_menu 

def main():
    root = tk.Tk()
    Barra_menu(root)

    app = UI(root=root)
    app.mainloop()
if __name__ == '__main__':
    main()

# Funciones DB
# def user():
    # mydb = mysql.connector.connect(
    #     host='localhost',
    #     user='root',
    #     password='',
    #     db='users'
    # )
    # r = mydb.cursor()
    # r.execute('SELECT * FROM user')
    # data = [db for db in r]
    # return data

# BarMenu funciones
# def _exit():
    # root.quit()
    # root.destroy()
    # exit()

# Menu
# barra_menu = tk.Menu(root)
# root.config(menu=barra_menu)
#Inicio
# menu_inicio = tk.Menu(barra_menu, tearoff=0)
# barra_menu.add_cascade(label='Archivo',menu=menu_inicio)
# menu_inicio.add_command(label='Salir', command=_exit)
# Editar
# menu_inicio = tk.Menu(barra_menu, tearoff=0)
# barra_menu.add_cascade(label='Editar',menu=menu_inicio)
# menu_inicio.add_command(label='Cortar', command=_exit)
# menu_inicio.add_command(label='Copiar', command=_exit)
# menu_inicio.add_command(label='Pegar', command=_exit)
# Ayuda
# menu_inicio = tk.Menu(barra_menu, tearoff=0)
# barra_menu.add_cascade(label='Ayuda',menu=menu_inicio)
# Label
# label1 = ttk.Label(root, text='Usuario')
# label2 = ttk.Label(root, text='Contraceña')
# Grid
# label1.grid(row=0,column=0)
# label2.grid(row=1,column=0)

# Frame
# tabla = ttk.Treeview(root,columns=('Usuarios','Contraseñas'),)
# tabla.grid(row=4,column=0, columnspan=3)
## Encabezados
# tabla.heading('#0',text='ID')
# tabla.heading('#1',text='Usuarios')
# tabla.heading('#2',text='Contraseñas')
# Valores de las columanas
# def display_db():
#     database = user()
#     database.reverse()
#     for i in database:
#         tabla.insert('',0,text=i[0],values=(i[1],i[2]))
# display_db()


# bt = ttk.Button(root,text='actualizar',command=display_db)
# bt.grid(row=2,column=0)
