from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Ruta del driver (asegúrate de tener chromedriver instalado)
driver_path = "C:/ruta/a/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Abrir WhatsApp Web
driver.get("https://web.whatsapp.com/")

# Espera hasta que la página cargue y aparezca la barra de búsqueda (max 30 segundos)
wait = WebDriverWait(driver, 30)
search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='3']")))

# Espera extra por si la página aún no termina de cargar (opcional)
time.sleep(5)

# Buscar contacto
contact_name = "+543644683871"
search_box.send_keys(contact_name)
time.sleep(2)  # pequeño retraso para que aparezca el contacto
contact = driver.find_element(By.XPATH, f"//span[@title='{contact_name}']")
contact.click()

# Escribir y enviar mensaje
message_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='10']")
message_box.send_keys("hola")
message_box.send_keys(u'\ue007')  # Enter para enviar

# Cerrar navegador (opcional)
# driver.quit()