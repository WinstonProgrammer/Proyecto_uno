import tkinter as tk
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
#Se crea canvas
lienzo = Canvas(root, width=1000, height=500)
lienzo.place(x=0, y=0)

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

#Se agregan imagenes al canvas
lienzo.create_image((1000, 500), image=imgFondo, anchor=SE)
lienzo.create_image((360, 175), image=imgLogo, anchor=NW)
lienzo.create_image((480, 30), image=imgWifi, anchor=NW)

#Boton Flecha Izquierda
Bt_FlechaIzq = Button(root, image=imgFlechaIzq, command=irIzquierda)
Bt_FlechaIzq.place(x=40,y=200)

#Boton Flecha Superior
Bt_FlechaSup = Button(root, repeatdelay=50, repeatinterval=50, image=imgFlechaSup, command=irAdelante)
Bt_FlechaSup.place(x=150,y=80)
Bt_FlechaSup.bind('<ButtonRelease-1>', soltar)

#Boton Flecha Derecha
Bt_FlechaDer = Button(root, image=imgFlechaDer, command=irDerecha)
Bt_FlechaDer.place(x=250,y=200)

#Boton Flecha Inferior
Bt_FlechaInf = Button(root, repeatdelay=50, repeatinterval=50, image=imgFlechaInf, command=irAtras)
Bt_FlechaInf.place(x=150,y=310)
Bt_FlechaInf.bind('<ButtonRelease-1>', soltar)

#Boton Stop
Bt_Stop = Button(root, image=imgDetener, command=stop)
Bt_Stop.place(x=148, y=195)

#Boton Apagar
Bt_Apagar = Button(root, image=imgApagar, command=root.destroy).place(x=435,y=370)

#Boton Lanzar
distancia = StringVar()
caja_distancia = tk.Entry(root, textvariable=distancia).place(x=700, y=370)
Bt_Lanzar = Button(root, image=imgLanzar, command= lambda: {tomar(distancia.get())})
Bt_Lanzar.place(x=700, y=160)


#Boton Conectar
button_connect = tk.Button(root, image=imgIniciar, command= lambda: {conectar(ev3_ip)}).place(x=419,y=70)


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
