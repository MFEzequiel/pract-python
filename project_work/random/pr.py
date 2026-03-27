try:
  import pyautogui
  import pywhatkit as kit
  import time
  import os
  from datetime import datetime as datatime
except ImportError as e:
  print("Error al importar módulos. Asegúrate de tener instaladas las librerías necesarias: ", e)

now = datatime.now()
hora = now.hour
minuto = now.minute + 1  # un minuto después de la hora actual

# Sintaxis: kit.sendwhatmsg("número", "mensaje", hora, minuto)
kit.sendwhatmsg("+543644683871", "Hola, este es un mensaje automático", hora, minuto)
# Esto abrirá WhatsApp Web en el navegador y enviará el mensaje a las 15:30 (hora local). Necesitas tener sesión iniciada en WhatsApp Web.