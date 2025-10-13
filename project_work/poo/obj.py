from abc import ABC, abstractmethod


# Definir como van a ser y que van a contener los objetos que creamos
class Users:
  def __init__(self, fullname, user, age):
    self._fullname = fullname # Atributo privado
    self.__user = user # Atributo muy privado
    self.age = age # Atributo público

  @property
  def name_user(self):
    return self.__user
  
  @name_user.setter
  def name_user(self, name):
    self.__user = name
      

user_one = Users("Marcelo","@ezequiel")
print(user_one._fullname) # se muestra en consola
print(user_one.__user) # genera un error


class Persona:
  def __init__(self, nombre, edad, nacionalidad):
    self.nombre = nombre
    self.edad = edad
    self.nacionalidad = nacionalidad

class Empleado(Persona):  # Empleado hereda de Persona
  def __init__(self, nombre, edad, salario):
    super().__init__(nombre, edad)
    self.salario = salario

persona1 = Persona('Ezequiel', 20, "argentino")