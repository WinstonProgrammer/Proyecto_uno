import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import socket


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

def parar():
    clientSocket.send(bytes([ord('t')]))

def inicioLanzar():
    clientSocket.send(bytes([ord('l')]))

def soltar(event):
    clientSocket.send(bytes([ord(' ')]))

#Interacción con el servidor
def getAddress():
    ip_root = Tk()
    ip_root.geometry("250x100")

    ip = StringVar(ip_root)
    ip_root.title("Configurar Ip")
    campo_ip = ttk.Entry(ip_root, textvariable=ip).place(x=10,y=10)
    bt_ip = Button(ip_root, text ="Aplicar",command=lambda:[conectar(ip.get()), ip_root.destroy()]).place(x=30,y=40)
    print(ip.get())

def conectar(address):
    port = 2222
    try:
        clientSocket.connect((address,port))
        messagebox.showinfo("Mensaje Servido","Cliente conectado al robot: {0} : {1}".format(address,port))
    except socket.error:
        messagebox.showwarning("Conexión erronea","No se ha logrado al conexíon, verifique la ip {0}".format(address))
        getAddress()
        clientSocket.close()

#Imagenes
imgLogo = tk.PhotoImage(file="logo_ant0t0.png")
imgFlechaIzq = tk.PhotoImage(file="flecha_izquierda.png")
imgFlechaSup = tk.PhotoImage(file="flecha_superior.png")
imgFlechaDer = tk.PhotoImage(file="flecha_derecha.png")
imgFlechaInf = tk.PhotoImage(file="flecha_inferior.png")
imgApagar = tk.PhotoImage(file="Boton_Apagar.png")

#Logo
etiqueta_logo = tk.Label(root, image=imgLogo, bg = "gray25").place(x=280,y=10)

#Boton Flecha Izquierda
Bt_FlechaIzq = Button(root, repeatdelay=50, repeatinterval=50, image=imgFlechaIzq, command=irIzquierda)
Bt_FlechaIzq.place(x=50,y=150)
Bt_FlechaIzq.bind('<ButtonRelease-1>', soltar)

#Boton Flecha Superior
Bt_FlechaSup = Button(root, repeatdelay=50, repeatinterval=50, image=imgFlechaSup, command=irAdelante)
Bt_FlechaSup.place(x=150,y=120)
Bt_FlechaSup.bind('<ButtonRelease-1>', soltar)

#Boton Flecha Derecha
Bt_FlechaDer = Button(root, repeatdelay=50, repeatinterval=50, image=imgFlechaDer, command=irDerecha)
Bt_FlechaDer.place(x=250,y=150)
Bt_FlechaDer.bind('<ButtonRelease-1>', soltar)

#Boton Flecha Inferior
Bt_FlechaInf = Button(root, repeatdelay=50, repeatinterval=50, image=imgFlechaInf, command=irAtras)
Bt_FlechaInf.place(x=150,y=250)
Bt_FlechaInf.bind('<ButtonRelease-1>', soltar)

#Boton de apagado
Bt_Apagar = Button(root, image=imgApagar, command=root.destroy).place(x=350,y=350)

#Boton Conectar
button_connect = tk.Button(root, text="Conectar", command=getAddress, font=("Arial",12)).place(x=350,y=260)

clientSocket = socket.socket()
port = 2222
ipAddress = "192.168.71.214"
root.mainloop()