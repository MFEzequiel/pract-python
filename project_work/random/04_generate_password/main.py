try:
  import string
  import random
except ImportError as e:
  print('Error al importar la libreria -->', e)

# length: longitud de la contraseña
# use_upper: incluir letras mayúsculas
# use_lower: incluir letras minúsculas
# use_digits: incluir dígitos
# use_special: incluir caracteres especiales
def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
  """Genera una contraseña segura basada en los criterios especificados."""
  if length < 4:
    raise ValueError("La longitud mínima de la contraseña debe ser 4.")

  character_pool = ""
  if use_upper:
    character_pool += string.ascii_uppercase
  if use_lower:
    character_pool += string.ascii_lowercase
  if use_digits:
    character_pool += string.digits
  if use_special:
    character_pool += string.punctuation

  if not character_pool:
    raise ValueError("Debe seleccionar al menos un tipo de carácter.")

  # Asegurar que la contraseña contenga al menos un carácter de cada tipo seleccionado
  password = []
  if use_upper:
    password.append(random.choice(string.ascii_uppercase))
  if use_lower:
    password.append(random.choice(string.ascii_lowercase))
  if use_digits:
    password.append(random.choice(string.digits))
  if use_special:
    password.append(random.choice(string.punctuation))

  # Rellenar el resto de la contraseña con caracteres aleatorios del pool
  while len(password) < length:
      password.append(random.choice(character_pool))

  random.shuffle(password)
  return ''.join(password)

if __name__ == "__main__":
  # Ejemplo de uso
  print("Contraseña generada:", generate_password(
    length=12,
    use_upper=True,
    use_lower=True,
    use_digits=True,
    use_special=True
  ))