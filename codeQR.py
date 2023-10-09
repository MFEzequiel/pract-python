import qrcode
import random

# Crear un número aleatorio de 10 dígitos
rand_num = random.randint(1000000000, 9999999999)

# Comvierte el número en una cadena
num_str = str(rand_num)

# Crear el códgo QR
img = qrcode.make(num_str)

# Guardar como img
img.save("codigo_qr_1.png")