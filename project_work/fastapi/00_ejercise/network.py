import socket

port = 8000

def get_host():
  get_socket_ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  try:
    # intenta determinar la IP local usando internet
    get_socket_ip.connect(("8.8.8.8", 80))
    host = get_socket_ip.getsockname()[0]
  except OSError:
    # si no hay conexión
    host = "127.0.0.1"
  finally:
    get_socket_ip.close()

  return host
