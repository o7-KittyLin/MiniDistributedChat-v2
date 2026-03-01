import socket
import threading

# Crear socket del cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Dirección del servidor
HOST = "192.168.1.52"
PUERTO = 5000

# Conectarse
cliente.connect((HOST, PUERTO))

# LOGIN
nombre = input("\n(ɔ◔‿◔)ɔ  Nombre: ")
cliente.send(f"LOGIN {nombre}".encode())

respuesta = cliente.recv(1024).decode()

if respuesta != "200 OK":
    print("\n(˶˃𐃷˂˶) Error de autenticación:", respuesta)
    cliente.close()
    exit()

print("\nAutenticación exitosa ദ്ദി◝ ⩊ ◜.ᐟ")

# JOIN
cliente.send(f"JOIN {nombre}".encode())

# Recibir mensajes
def recibir():
    while True:
        try:
            mensaje = cliente.recv(1024).decode()
            if not mensaje:
                break
            print("\n" + mensaje)
        except:
            print("\n(¬⤙¬ ) Desconectado del servidor.")
            break

threading.Thread(target=recibir, daemon=True).start()

# Enviar mensajes
while True:
    texto = input()

    if texto.upper() == "EXIT":
        cliente.send("EXIT".encode())
        break

    cliente.send(f"MSG {texto}".encode())

cliente.close()