import qrcode
import random

# Crear un número aleatorio de 10 dígitos
rand_num = random.randint(1000000000, 9999999999)

# Comvierte el número en una cadena
print("Materia, Profesor, Alumno")
mat = "Practica Profesionalizante"
prof = "Rocha Facundo"
alum = input()

data = datos = f" Materia: {mat}\nProfesor: {prof}\nAlumno: {alum}"

# Crear el códgo QR
img = qrcode.make(data)

# Guardar como img
img.save("data.png")