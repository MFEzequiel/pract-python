# -*- coding: utf-8 -*-
try:
  from pack import sec, matris, class_and_obj
except ImportError as e:
  print('Error importando modulos: ', e)

print('\n',sec.celular1_camaraF,'\n')
print('\n',matris.celulares,'\n')
print('\n',class_and_obj.Celular.celular1_camaraF,'\n')

'''
  Crea una app con kivy usando sqlite, pandas, os, módulos y poo, herencia , abstracción, polimorfismo y encapsulación, getter y setter, el cual tendrá los paquetes core, db y ui, agrega algunos q creas convenientes, config.py utilizara las rutas donde se guardara la db y el file excel, en la interfaz abra un formulario donde se podrán cargar mas datos, en este caso serán un kiosco el cual puede ver los productos, el precio el stock y el detalle de dicho producto al igual de poder agregar mas campos en caso de ser necesarios, los clientes que pagan y los q deben y los proveedores, en el menú se podrá seleccionar distintas opciones, entre las cuales esta el browser sql q le permitirá ver las tablas de la db y sus datos, también podrá seleccionar una calculadora el cual tome el costo del producto y el precio de venta y una opción de selección para descuentos 0, 5, 10, 20, 30, 40, 50, 60, 70, 80 y 90 %, una opción q permita escribir cuanto es el impuesto a pagar ,el cual deberá evaluar el costo y el porcentaje, impuesto y ganancia, ademas, el menú tendra una opción el cual permitira decidir el puerto por donde se coparte la db a los dispositios conectados a dicha red.
'''