#!/usr/bin/env python3
import socket
from funciones import *

#se crea un socket
s = socket.socket()
s.settimeout(20)
print("Socket creado")
port = 2222
#se asocia una direccion IP y un numero de puerto al socket
s.bind(("", port))
print("El socket se creo con puerto:{}".format(port))
#se comienza a escuchar conexiones entrantes (maximo 5 conexiones pendientes)
s.listen(5)
print("The socket is listening....")
#se acepta la conexion, creando un nuevo socket a partir de la conexion entrante y la direccion del cliente
connect, addr = s.accept()
print("Se conecto a {}".format(addr))
while True:
    #se define el caracter que el socket del cliente recibe como dato
    rawByte = connect.recv(1)
    #se traduce el caracter recibido
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
        rawByte = connect.recv(1)
        distancia = rawByte.decode('utf-8')

        lanzar(float(distancia))
