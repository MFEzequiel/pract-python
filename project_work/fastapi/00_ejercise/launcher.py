import tkinter as tk
from threading import Thread
import uvicorn
import server.app as server
import network
import config as cg

cg.create_folder()

# Variable para manejar el servidor
server_thread = None

# Función para iniciar el servidor en un thread
def start_server():
  host_ip = network.get_host()
  global server_thread
  if server_thread is None or not server_thread.is_alive():
    server_thread = Thread(
      target=lambda: uvicorn.run(
        server.app,
        host=host_ip,
        port=network.port,
        log_level="info",
        reload=False
      )
    )
    server_thread.daemon = True
    server_thread.start()
    status_label_1.config(text=f"Servidor iniciado en http://{host_ip}:{network.port}")
    text_status.set(f"http://{host_ip}:{network.port}/assistence")
  else:
    status_label_1.config(text="El servidor ya está corriendo")
    text_status.set("El servidor ya está corriendo")
    pass

# Función para detener el servidor (muy básico, solo feedback)
def stop_server():
  # Uvicorn no tiene un stop oficial desde otro thread, esto es solo para el GUI
  status_label_1.config(text="Para detener el servidor, cierra la aplicación.")

# GUI con Tkinter
root = tk.Tk()
root.title("Server Manager")

start_btn = tk.Button(root, text="Iniciar Servidor", command=start_server)
start_btn.pack(pady=10)

stop_btn = tk.Button(root, text="Detener Servidor", command=stop_server)
stop_btn.pack(pady=10)

text_status = tk.StringVar()
status_label_1 = tk.Label(root, text='Servidor iniciado')
status_label_1.pack(pady=10)
status_label_2 = tk.Entry(root, width=50, textvariable=text_status)
status_label_2.pack(pady=10)

root.mainloop()
  
