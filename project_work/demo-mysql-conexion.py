import tkinter as tk
import tkinter as ttk
import mysql.connector


def connect_db():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = ""
    )
    showdb = mydb.cursor()
    showdb.execute("SHOW DATABASES")
    database = [db[0] for db in showdb]
    mydb.close()
    return database


def display_db():
    database = connect_db()
    for idx, db in enumerate(database):
        label = ttk.Label(root, text=db)
        label.grid(column=0,row=idx)
    pass

# Iniciar root
root = tk.Tk()
root.title("Python-MySQL")

# Menu
bmenu = tk.Menu(root)
root.config(menu=bmenu)

# Opciones del menu
op_menu = tk.Menu(bmenu)
op_menu.add_command(label="Nuevo")
bmenu.add_cascade(label="Archivo", menu=op_menu)


# Etiquetas

# LLamar a la function
display_db()

root.mainloop()