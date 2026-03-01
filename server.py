import socket
import threading

# Crear socket del servidor (IPv4 + TCP)
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Dirección y puerto donde escuchará el servidor
HOST = "0.0.0.0"
PUERTO = 5000

# Enlazar el socket a la dirección y puerto
servidor.bind((HOST, PUERTO))

# Poner el servidor en modo escucha
servidor.listen()

print(f"\nᓚ₍⑅^..^₎♡ Servidor activo en {HOST}:{PUERTO}")

# Estado compartido del sistema
clientes = []
nombres = {}

# Función de Broadcast -> Envía mensaje a todos menos al remitente
def broadcast(mensaje, remitente=None):
    for cliente in clientes[:]:
        if cliente != remitente:
            try:
                cliente.send(mensaje.encode())
            except:
                # Manejo de fallo si un cliente se desconecta inesperadamente
                clientes.remove(cliente)
                nombres.pop(cliente, None)
                cliente.close()

# Función que maneja cada cliente
def manejar_cliente(cliente):

    autenticado = False
    nombre = None

    while True:
        try:
            # Recibir mensaje del cliente
            msg = cliente.recv(1024).decode()

            if not msg:
                break

            print(f"\nRAW recibido: {msg}")

            # LOGIN <nombre>
            if msg.startswith("LOGIN"):

                login = msg.split(" ", 1)[1].strip()

                # Validar que el nombre no esté vacío y no esté repetido
                if login and login not in nombres.values():

                    cliente.send("200 OK".encode())
                    print(f"\nദ്ദി(˵ •̀ ᴗ - ˵ ) ✧ LOGIN exitoso para {login}")

                    autenticado = True
                    nombre = login

                else:
                    cliente.send("401 ERROR".encode())
                    print(f"\n(˶°ㅁ°)!! LOGIN fallido para {login}")

                continue

            # JOIN -> Solo si ya hizo LOGIN
            if msg.startswith("JOIN") and autenticado:

                nombres[cliente] = nombre
                clientes.append(cliente)

                broadcast(f"(っˆ▿ˆ)☞ {nombre} se unió al chat ₍^. .^₎⟆")
                continue

            # MSG
            if msg.startswith("MSG") and autenticado:

                texto = msg.split(" ", 1)[1]

                print(f"\n{nombre}: {texto}")

                broadcast(f"{nombre}: {texto}", remitente=cliente)
                continue

            # EXIT
            if msg.startswith("EXIT"):
                break

        except:
            break

    # Limpieza al desconectarse
    nombre = nombres.get(cliente, "Alguien")

    if cliente in clientes:
        clientes.remove(cliente)

    nombres.pop(cliente, None)

    broadcast(f"\n(˶°ㅁ°)!! {nombre} salió del chat.")

    cliente.close()

    print(f"\n(⇀‸↼‶) {nombre} se desconectó.")

# Hilo para que el servidor también pueda enviar mensajes
def consola_servidor():
    while True:
        texto = input()
        if texto:
            broadcast(f"Servidor: {texto}")

# Iniciar hilo de consola del servidor
threading.Thread(target=consola_servidor, daemon=True).start()

# Bucle principal para aceptar conexiones
while True:
    cliente, addr = servidor.accept()
    print("\nConexión recibida desde:", addr)

    # Crear hilo independiente por cliente
    threading.Thread(
        target=manejar_cliente,
        args=(cliente,),
        daemon=True
    ).start()