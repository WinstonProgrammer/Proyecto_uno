import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import socket
import time
import sys

ev3_ip = "192.168.70.147"

#Ventana
root = tk.Tk()
root.config(width=1000, height=500)
root.config(bg="darkred")
root.title("ANT-0T0")

#Acciones del robot
def irAdelante():
    clientSocket.send(bytes([ord('w')]))

def irAtras():
    clientSocket.send(bytes([ord('s')]))
    
def irIzquierda():
    clientSocket.send(bytes([ord('a')]))

def irDerecha():
    clientSocket.send(bytes([ord('d')]))

def inicioLanzar():
    clientSocket.send(bytes([ord('l')]))

def soltar(event):
    clientSocket.send(bytes([ord(' ')]))

def conectar(address):
    try:
        clientSocket.connect((address,port))
        messagebox.showinfo("Mensaje Servido","Cliente conectado al robot: {0} : {1}".format(address,port))
    except socket.error:
        messagebox.showwarning("Conexión erronea","No se ha logrado al conexíon, verifique la ip {0}".format(address))
        clientSocket.close()
    

#Imagenes
imgLogo = tk.PhotoImage(file="logo_ant0t0.png")
imgFlechaIzq = tk.PhotoImage(file="flecha_izquierda.png")
imgFlechaSup = tk.PhotoImage(file="flecha_superior.png")
imgFlechaDer = tk.PhotoImage(file="flecha_derecha.png")
imgFlechaInf = tk.PhotoImage(file="flecha_inferior.png")
imgApagar = tk.PhotoImage(file="Boton_Apagar.png")
imgLanzar = tk.PhotoImage(file="imgLanzar.png")

etiqueta_logo = tk.Label(root, image=imgLogo, bg = "darkred").place(x=350,y=150)
#Boton Flecha Izquierda
Bt_FlechaIzq = Button(root, repeatdelay=50, repeatinterval=50, image=imgFlechaIzq, command=irIzquierda)
Bt_FlechaIzq.place(x=50,y=190)
Bt_FlechaIzq.bind('<ButtonRelease-1>', soltar)
#Boton Flecha Superior
Bt_FlechaSup = Button(root, repeatdelay=50, repeatinterval=50, image=imgFlechaSup, command=irAdelante)
Bt_FlechaSup.place(x=150,y=100)
Bt_FlechaSup.bind('<ButtonRelease-1>', soltar)
#Boton Flecha Derecha
Bt_FlechaDer = Button(root, repeatdelay=50, repeatinterval=50, image=imgFlechaDer, command=irDerecha)
Bt_FlechaDer.place(x=250,y=190)
Bt_FlechaDer.bind('<ButtonRelease-1>', soltar)
#Boton Flecha Inferior
Bt_FlechaInf = Button(root, repeatdelay=50, repeatinterval=50, image=imgFlechaInf, command=irAtras)
Bt_FlechaInf.place(x=150,y=280)
Bt_FlechaInf.bind('<ButtonRelease-1>', soltar)

#Boton Apagado
Bt_Apagar = Button(root, image=imgApagar, command=root.destroy).place(x=440,y=370)

#Boton Lanzar
Bt_Lanzar = Button(root, image=imgLanzar, bg = "darkred", command=inicioLanzar)
Bt_Lanzar.place(x=650, y=210)

#Boton Conectar
button_connect = tk.Button(root, text="Conectar", command= lambda: {conectar(ev3_ip)}, font=("Arial",12)).place(x=440,y=90)


if len(sys.argv) > 2:
    print("usage:client-laptop,py [IP-addr-of-robot]")
    sys.exit(1)

elif len(sys.argv) == 2:
    ipAddress = sys.argv[1]
    print("using specified IP address: {}".format(ipAddress))

else:
    print("using default IP address: {}".format(ev3_ip))
    
clientSocket = socket.socket()
port = 2222

root.mainloop()