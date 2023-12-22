import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import socket
import sys

clientSocket = socket.socket()
ev3_ip = "192.168.71.76"

#Ventana
root = tk.Tk()
root.config(width=1000, height=500)
root.config(bg="darkred")
root.title("ANT-0T0")
root.resizable(False, False)

#Acciones del robot
def irAdelante():
    clientSocket.send(bytes([ord('w')]))

def irAtras():
    clientSocket.send(bytes([ord('s')]))
    
def irIzquierda():
    clientSocket.send(bytes([ord('a')]))

def irDerecha():
    clientSocket.send(bytes([ord('d')]))

def inicioLanzar(distancia):
    clientSocket.send(bytes([ord('l')]))
    clientSocket.send(bytes(distancia, encoding='utf-8'))

def stop():
    clientSocket.send(bytes([ord(' ')]))
    
def soltar(event):
    clientSocket.send(bytes([ord(' ')]))

def conectar(address):
    try:
        clientSocket.connect((address,port))
        messagebox.showinfo("Mensaje Servido","Cliente conectado al robot: {0} : {1}".format(address,port))
    except socket.error:
        messagebox.showwarning("Conexión erronea","No se ha logrado al conexíon, verifique la ip {0}".format(address))
        clientSocket.close()

def tomar(valor):
    try:
        inicioLanzar(valor)
        float(valor)
    except ValueError:
        messagebox.showerror("Error", "Debe ingresar un valor númerico para la distancia")
    

#Imagenes
imgFondo = tk.PhotoImage(file="FondoInterfaz.png")
imgIniciar = tk.PhotoImage(file="BotonStart.png")
imgWifi = tk.PhotoImage(file="Wifi.png")
imgLogo = tk.PhotoImage(file="logo_ant0t0.png")
imgFlechaIzq = tk.PhotoImage(file="FlechaIzquierda.png")
imgFlechaSup = tk.PhotoImage(file="FlechaArriba.png")
imgFlechaDer = tk.PhotoImage(file="FlechaDerecha.png")
imgFlechaInf = tk.PhotoImage(file="FlechaInferior.png")
imgApagar = tk.PhotoImage(file="BotonApagar(Rojo).png")
imgLanzar = tk.PhotoImage(file="BotonDisparo(Rojo).png")
imgDetener = tk.PhotoImage(file="BotonDetener(Verde).png")

distancia = StringVar()
caja_distancia = tk.Entry(root, textvariable=distancia).place(x=680, y=370)

etiqueta_fondo = tk.Label(root, image=imgFondo)
etiqueta_fondo.pack()

etiqueta_logo = tk.Label(root, image=imgLogo).place(x=350,y=150)

#Boton Flecha Izquierda
Bt_FlechaIzq = Button(root, image=imgFlechaIzq, command=irIzquierda)
Bt_FlechaIzq.place(x=50,y=190)

#Boton Flecha Superior
Bt_FlechaSup = Button(root, repeatdelay=50, repeatinterval=50, image=imgFlechaSup, command=irAdelante)
Bt_FlechaSup.place(x=150,y=100)
Bt_FlechaSup.bind('<ButtonRelease-1>', soltar)

#Boton Flecha Derecha
Bt_FlechaDer = Button(root, image=imgFlechaDer, command=irDerecha)
Bt_FlechaDer.place(x=250,y=190)

#Boton Flecha Inferior
Bt_FlechaInf = Button(root, repeatdelay=50, repeatinterval=50, image=imgFlechaInf, command=irAtras)
Bt_FlechaInf.place(x=150,y=280)
Bt_FlechaInf.bind('<ButtonRelease-1>', soltar)

#Boton Stop
Bt_Stop = Button(root, image=imgDetener, command=stop)
Bt_Stop.place(x=175, y=210)

#Boton Apagado
Bt_Apagar = Button(root, image=imgApagar, command=root.destroy).place(x=440,y=370)

#Boton Lanzar
Bt_Lanzar = Button(root, image=imgLanzar, command= lambda: {tomar(distancia.get())})
Bt_Lanzar.place(x=680, y=160)


#Boton Conectar
button_connect = tk.Button(root, image=imgIniciar, command= lambda: {conectar(ev3_ip)}, font=("Arial",12)).place(x=420,y=70)


if len(sys.argv) > 2:
    print("usage:client-laptop,py [IP-addr-of-robot]")
    sys.exit(1)

elif len(sys.argv) == 2:
    ipAddress = sys.argv[1]
    print("using specified IP address: {}".format(ipAddress))

else:
    print("using default IP address: {}".format(ev3_ip))

port = 2222

root.mainloop()