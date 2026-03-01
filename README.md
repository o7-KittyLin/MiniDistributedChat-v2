📄 **Estructura basada en:**
La guía para crear READMEs profesionales de DevXP ([https://github.com/Organization-DevXP/Guia-para-crear-READMEs-Profesionales](https://github.com/Organization-DevXP/Guia-para-crear-READMEs-Profesionales))

# MiniChatProtocol v2 🔐💬

## Descripción

MiniChatProtocol v2 es una aplicación de chat distribuido desarrollada en **Python**, que implementa un protocolo básico inspirado en HTTP mediante el modelo **Request–Response**.

El sistema utiliza sockets TCP y un servidor concurrente basado en `threading`, capaz de gestionar múltiples clientes simultáneamente, autenticación mediante comando `LOGIN` y códigos de estado (`200 OK`, `401 ERROR`).

Este proyecto corresponde a la **Parte 6 – Mini Ejercicio Práctico** de la materia *Sistemas Distribuidos*, donde se aplican los conceptos de:

* Cliente–Servidor
* Request–Response
* Simulación de códigos tipo HTTP
* Concurrencia
* Estado compartido

## 🚀 ¿Qué encontrarás aquí?

* **Servidor concurrente** usando `threading`
* **Autenticación simulada tipo HTTP**

  * `LOGIN <nombre>`
  * Respuesta: `200 OK` o `401 ERROR`
* **Control de nombres únicos**
* **Protocolo estructurado**

  * `LOGIN`
  * `JOIN`
  * `MSG`
  * `EXIT`
* **Broadcast a múltiples clientes**
* **Manejo de desconexiones inesperadas**
* **Consola activa del servidor** para enviar mensajes manuales
* **Simulación del modelo Request–Response**

## 🎯 Objetivo del Taller

Aplicar los conceptos de:

* Modelo Cliente–Servidor
* Patrón Request–Response
* Simulación de códigos de estado tipo HTTP
* Concurrencia con múltiples clientes
* Comparación conceptual con P2P
* Comprensión del Modelo de 3 Capas como base para sistemas escalables

Además, modificar el cliente-servidor anterior para implementar un protocolo con autenticación estructurada:

```
Cliente → LOGIN Juan
Servidor → 200 OK | 401 ERROR
```

## 👩‍💻 ¿A quién está dirigido?

* Estudiantes de Sistemas Distribuidos
* Personas que estén aprendiendo sockets en Python
* Quienes deseen entender cómo funcionan los protocolos tipo HTTP
* Desarrolladores interesados en arquitectura Cliente–Servidor

## 📂 Estructura del Proyecto

```
MiniChatProtocol/
│
├── server.py     # Servidor concurrente con autenticación
├── client.py     # Cliente TCP interactivo
└── README.md
```

# ⚙️ Instalación

## 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/MiniChatProtocol.git
```

Luego:

```bash
cd MiniChatProtocol
```

## 2️⃣ Verificar Python

Requiere **Python 3.8 o superior**

```bash
python --version
```

# 🖥️ Configuración de Red 🌐

El servidor utiliza:

```
HOST = "0.0.0.0"
PUERTO = 5000
```

Esto significa que escucha en todas las interfaces disponibles.

## Obtener IP del servidor

### Windows

```bash
ipconfig
```

### Linux / Mac

```bash
ifconfig
```

Busca la dirección IPv4, por ejemplo:

```
192.168.1.52
```

## 🔧 Configurar el Cliente

En `client.py`, cambia:

```
HOST = "192.168.1.52"
```

Por la IP real del computador que ejecuta el servidor.

⚠️ Si no actualizas la IP correctamente, el cliente no podrá conectarse.

# ▶️ Instrucciones de Ejecución 🚀

## 1️⃣ Ejecutar el servidor

```bash
python server.py
```

El servidor comenzará a aceptar múltiples conexiones simultáneamente.

## 2️⃣ Ejecutar el cliente

```bash
python client.py
```

* Ingresa tu nombre cuando lo solicite
* Si el nombre ya está en uso, recibirás `401 ERROR`
* Si es válido, recibirás `200 OK`

Puedes abrir múltiples clientes simultáneamente.

# 📜 Protocolo de Comunicación

El sistema implementa el siguiente protocolo:

## 🔹 LOGIN (Autenticación)

```
LOGIN <nombre>
```

Servidor responde:

```
200 OK
```

o

```
401 ERROR
```

## 🔹 JOIN (Unirse al chat)

```
JOIN <nombre>
```

Solo permitido después de autenticación exitosa.

## 🔹 Enviar mensaje

```
MSG <texto>
```

Ejemplo:

```
MSG Hola a todos
```

## 🔹 Salir del chat

```
EXIT
```

# 🧠 Funcionamiento Interno

El servidor:

* Crea un hilo independiente por cada cliente 🧵
* Valida autenticación antes de permitir acceso
* Controla nombres únicos activos
* Mantiene estado compartido mediante listas y diccionarios
* Implementa patrón Request–Response
* Simula códigos de estado HTTP
* Reenvía mensajes a todos los clientes conectados
* Maneja fallos y desconexiones automáticamente
* Permite enviar mensajes desde la consola del servidor

# 🏗️ Modelo Arquitectónico Aplicado

### 🔹 Cliente–Servidor

El servidor central gestiona conexiones y estado global.

### 🔹 Request–Response

Cada solicitud del cliente genera una respuesta explícita del servidor (LOGIN → 200/401).

### 🔹 Diferencia con P2P

En este sistema:

* Los clientes no se comunican entre sí directamente.
* Todo pasa por el servidor central.

En P2P, cada nodo puede actuar como cliente y servidor simultáneamente.

### 🔹 Relación con el Modelo de 3 Capas

Aunque es un sistema simple, se puede conceptualizar como:

* Capa de Presentación → Cliente
* Capa de Lógica → Servidor
* Capa de Datos → Estructuras compartidas (memoria)

Esto permite entender cómo escalar hacia arquitecturas más complejas.

# 🌐 Prueba en Red LAN

Para validar funcionamiento real:

1. Ejecutar servidor en Computador A.
2. Obtener su IP local.
3. Desde Computador B (misma red), ejecutar cliente.
4. Conectarse usando la IP real.
5. Validar autenticación y envío de mensajes en tiempo real.

✔️ Soporte para múltiples clientes simultáneos
✔️ Manejo de autenticación
✔️ Broadcast funcional

# ✅ Estado del Proyecto

* Autenticación tipo HTTP implementada
* Códigos de estado simulados
* Servidor concurrente funcional
* Broadcast operativo
* Manejo de desconexiones
* Validación en entorno LAN

# 🎓 Conclusión

MiniChatProtocol v2 permitió comprender de forma práctica:

* Cómo funciona el modelo Cliente–Servidor
* Cómo opera el patrón Request–Response
* Cómo se estructuran protocolos tipo HTTP
* Cómo manejar múltiples clientes concurrentemente
* Cuándo usar Cliente–Servidor y cuándo P2P
* Cómo el modelo de 3 capas favorece la escalabilidad

El ejercicio demuestra que incluso un sistema pequeño puede reflejar principios fundamentales de arquitectura distribuida.
* Agregar badges (Python, License, Status)
* O ayudarte a redactar la conclusión en tono más académico tipo informe 👀
