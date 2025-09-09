import mysql.connector
import tkinter as tk
from tkinter import ttk 

db = mysql.connector.connect(
  host = 'localhost',
  port = '3306',
  user = 'root',
  password = '',
  database = 'py_user'
)

mycursor = db.cursor()

def show_data():
  sql = 'SELECT id, name FROM user'
  mycursor.execute(sql)
  result = mycursor.fetchall()

  for data in result:
    table.insert("", tk.END, values=data)


def new_user():
  insert = 'INSERT INTO user (id, name) VALUES (%s, %s)'

  val = (1, insert_name.get())
  
  mycursor.execute(insert, val)

  db.commit()

  print(mycursor.rowcount)

  show_data()


root = tk.Tk()

# Create teble
table = ttk.Treeview(root)

# Define columns
table["columns"] = ('Id','Nombre', 'Apellido')

# Formate teble
table.column('#0', width=0, stretch=tk.NO)
table.column('Nombre', width=100, stretch=tk.NO)
table.column('Apellido', width=100, stretch=tk.NO)

# Create headings
table.heading('#0', text='', anchor=tk.W)
table.heading('Id', text='Id', anchor=tk.W)
table.heading('Nombre', text='Nombre', anchor=tk.W)
table.heading('Apellido', text='Apellido', anchor=tk.W)

# Create label
label_name = tk.StringVar()
insert_name = ttk.Entry(root, width=20,textvariable=label_name)
# Create buttons
bt_save = ttk.Button(root, text='Gurdar', command=new_user)


# Position elements
table.grid(column=0, row=1)
insert_name.grid(column=1, row=0)
bt_save.grid(column=0, row=0)

show_data()

root.mainloop()