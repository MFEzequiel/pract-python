# -*- coding: utf-8 *-*
import tkinter as tk
from tkinter import ttk
from modulos.connectdao.dao import DAO


def Barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu)
    #Inicio
    menu_file = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Archivo',menu=menu_file)
    menu_file.add_command(label='Crear Registro')
    menu_file.add_command(label='Eliminar Registro')
    menu_file.add_separator()
    menu_file.add_command(label='Salir', command=root.destroy)

    # Editar
    menu_edit = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Editar',menu=menu_edit)
    menu_edit.add_command(label='Cortar')

    # Ayuda
    menu_ayuda = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Ayuda', menu=menu_ayuda)
    menu_ayuda.add_command(label='Acerca de')


class UI(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root,width=480,height=320)
        self.root = root
        self.pack()

        self.img()
        self.disabled_entry()
        self.tables()
    
    def img(self):

        self.label_img = tk.Label(self, text='Imagen')
        self.label_img.config(font=('Arial', 12, 'bold'))
        self.label_img.grid(column=0, row=0, pady=10)

        
        self.title = tk.Label(self, text='Nombre')
        self.title.config(font=('Arial', 12, 'bold'))
        self.title.grid(column=0, row=1, pady=10)
        
        self.desc = tk.Label(self, text='Descripción')
        self.desc.config(font=('Arial', 12, 'bold'))
        self.desc.grid(column=0, row=2, pady=10)
        
        self.val = tk.Label(self, text='Preció')
        self.val.config(font=('Arial', 12, 'bold'))
        self.val.grid(column=0, row=3, pady=10)

        self.strv = tk.StringVar() 
        self.entry_title = tk.Entry(self, textvariable=self.strv)
        self.entry_title.config(width=25)
        self.entry_title.grid(column=1, row=1,)

        self.strv1 = tk.StringVar() 
        self.entry_desc = tk.Entry(self, textvariable=self.strv1)
        self.entry_desc.config(width=25)
        self.entry_desc.grid(column=1, row=2)

        self.strv2 = tk.StringVar() 
        self.entry_val = tk.Entry(self, textvariable=self.strv2)
        self.entry_val.config(width=25)
        self.entry_val.grid(column=1, row=3)
        
        self.bt_new = tk.Button(self, text='Nuevo', command=self.enabled_entry)
        self.bt_new.config(font=('Arial',12, 'bold'), bg='#131', fg='#fff', cursor="hand2")
        self.bt_new.grid(column=0,row=4, padx=5, pady=5)

        self.bt_save = tk.Button(self, text='Guardar', command=self.save)
        self.bt_save.config(font=('Arial',12, 'bold'), bg='#131', fg='#fff', cursor="hand2")
        self.bt_save.grid(column=1,row=4, padx=5, pady=5)

        self.bt_cancelar = tk.Button(self, text='Cancelar', command=self.disabled_entry)
        self.bt_cancelar.config(font=('Arial',12, 'bold'), bg='#131', fg='#fff', cursor="hand2")
        self.bt_cancelar.grid(column=2,row=4, padx=5, pady=5)

    def enabled_entry(self):
        self.strv.set('')
        self.strv1.set('')
        self.strv2.set('')

        self.entry_title.config(state='normal')
        self.entry_desc.config(state='normal')
        self.entry_val.config(state='normal')

        self.bt_save.config(state='normal')
        self.bt_cancelar.config(state='normal')

    def disabled_entry(self):
        self.strv.set('')
        self.strv1.set('')
        self.strv2.set('')

        self.entry_title.config(state='disabled')
        self.entry_desc.config(state='disabled')
        self.entry_val.config(state='disabled')

        self.bt_save.config(state='disabled')
        self.bt_cancelar.config(state='disabled')
    
    def save(self):
        
        self.disabled_entry()

    def tables(self):
        self.tablas = ttk.Treeview(self, column=('Imagen', 'Nombre', 'Descripción', 'Valor'))
        self.tablas.grid(column=0, row=5, columnspan=5)
        self.tablas.heading('#0', text='ID')
        self.tablas.heading('#1', text='Imagen')
        self.tablas.heading('#2', text='Nombre')
        self.tablas.heading('#3', text='Descripción')
        self.tablas.heading('#4', text='Valor')

        self.bt_edit = tk.Button(self, text='Editar', command=self.enabled_entry)
        self.bt_edit.config(font=('Arial',12, 'bold'), bg='#131', fg='#fff', cursor="hand2")
        self.bt_edit.grid(column=0,row=6, padx=5, pady=5)

        self.bt_delate = tk.Button(self, text='Elimiar', command=self.enabled_entry)
        self.bt_delate.config(font=('Arial',12, 'bold'), bg='#131', fg='#fff', cursor="hand2")
        self.bt_delate.grid(column=1,row=6, padx=5, pady=5)
    
    def list_optioin(self):
        self.cont = DAO()

        self.tablas.insert('',0,text=i[0],value=(i[1],i[2],i[3],i[4]))