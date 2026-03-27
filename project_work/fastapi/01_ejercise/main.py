from threading import Thread
import uvicorn
import network as net
from tkinter import Tk, ttk, StringVar

# Variable para manejar el servidor
server_thread = None

def start_server():
  host_ip = net.get_host()
  global server_thread
  if server_thread is None or not server_thread.is_alive():
    server_thread = Thread(
      target=lambda: uvicorn.run(
        'app:app',
        host=host_ip,
        port=net.port,
        log_level="info",
        reload=False
      )
    )
    server_thread.daemon = True
    server_thread.start()
    status_label_1.config(text=f"Servidor iniciado en http://{host_ip}:{net.port}")
    text_status.set(f"http://{host_ip}:{net.port}/assistence")
  else:
    status_label_1.config(text="El servidor ya está corriendo")
    text_status.set("El servidor ya está corriendo")
    pass

# Función para detener el servidor (muy básico, solo feedback)
def stop_server():
  # Uvicorn no tiene un stop oficial desde otro thread, esto es solo para el GUI
  status_label_1.config(text="Para detener el servidor, cierra la aplicación.")

# GUI con Tkinter
root = Tk()
root.title("Server Manager")

start_btn = ttk.Button(root, text="Iniciar Servidor", command=start_server)
start_btn.pack(pady=10)

stop_btn = ttk.Button(root, text="Detener Servidor", command=stop_server)
stop_btn.pack(pady=10)

text_status = StringVar()
status_label_1 = ttk.Label(root, text='Servidor iniciado')
status_label_1.pack(pady=10)
status_label_2 = ttk.Entry(root, width=50, textvariable=text_status)
status_label_2.pack(pady=10)

root.mainloop()

# if __name__ == "__main__":
#   host = net.get_host()
#   print(f"Servidor disponible en: http://{host}:{net.port}")
#   uvicorn.run(
#   "main:app",
#   host=host,
#   port=net.port,
#   reload=True
#   )