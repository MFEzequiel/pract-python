# Definir como van a ser y que van a contener los objetos que creamos
class Users:
    def __init__(self, fullname, user):
        self.fullname = fullname
        self.user = user

intance = Users("Marcelo","@ezequiel") # el object "intance" es una instancia de una class / para crear un objeto de la class Users
print(intance.fullname) 