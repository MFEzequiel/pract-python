import mysql.connector
from mysql.connector import Error


class DAO():
    def __init__(self):
        try:
            self.conection = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = '',
                db = 'products'
            )
        except Error as er:
            print('Error al intetar la conexión: {0}'.format(er))
        self.list_product()
    
    def list_product(self):
        if self.conection.is_connected():
            try:   
                self.product = self.conection.cursor()
                self.product.execute('SELECT * FROM product ORDER BY ID ASC')
                self.result = self.product.fetchall()
                return self.result
            except Error as er:
                print('Error al intetar la conexión: {0}'.format(er))