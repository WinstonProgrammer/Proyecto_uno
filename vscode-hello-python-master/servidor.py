import socket
from demo import *

#se crea un socket
s = socket.socket()
print("Socket creado")
port = 2222
#se asocia una dirección IP y un número de puerto al socket
s.bind(("", port))
print("El socket se creo con puerto:{}".format(port))
#se comienza a escuchar conexiones entrantes (máximo 5 conexiones pendientes)
s.listen(5)
print("The socket is listening....")
#se acepta la conexión, creando un nuevo socket a partir de la conexion entrante y la dirección del cliente
connect, addr = s.accept()
print("Se conecto a {}".format(addr))
while True:
    #se define el carácter que el socket del cliente recibe como dato
    rawByte = connect.recv(1)
    #se traduce el carácter recibido
    char = rawByte.decode('utf-8')
    if (char == 'w'):
        mover_adelante()
    if (char == 's'):
        mover_atras()
    if (char == 'a'):
        mover_izquierda()
    if (char == 'd'):
        mover_derecha()
    if (char == ' '):
        detener()
    if (char == 'l'):
        lanzar(2)
