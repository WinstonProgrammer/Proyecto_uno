import tkinter as tk
from tkinter import ttk
from tkinter import *
import socket 


#Ventana
ventana = tk.Tk()
ventana.config(width=900, height=700)
ventana.title("Interfaz -> Gorilla-Tank")
ventana.configure(bg="gray25")


#FUNCIONES
def Arriba(event= None):
    clientSocket.send(bytes([ord('w')]))
    
def Abajo(event=None):
    clientSocket.send(bytes([ord('s')]))
    
def Izquierda(event=None):
    clientSocket.send(bytes([ord('a')]))

def Derecha(event=None):
    clientSocket.send(bytes([ord('d')]))

def Disparar(event=None):
    clientSocket.send(bytes([ord('p')]))

def Angulo():
    if(opcion.get()=="45"):
        clientSocket.send(bytes([ord('i')]))
    elif(opcion.get() == "0"):
        clientSocket.send(bytes([ord('o')]))

def Luciano():
    clientSocket.send(bytes([ord('f')]))
    
def Distancia():
    clientSocket.send(bytes([ord('m')]))
def on_realese(event):
    print("click realese")
    clientSocket.send(bytes([ord(' ')]))
def Cannon(event):
    clientSocket.send(bytes([ord('l')]))

def getAddres():
    w_ip = Tk()
    w_ip.geometry("300x100")

    dato = StringVar(w_ip)
    w_ip.title("Configurar Ip")
    ip = ttk.Entry(w_ip,textvariable=dato).place(x=10,y=10)
    button = Button(w_ip,text =" Aplicar",command=lambda:[conectar(dato.get()),w_ip.destroy()]).place(x=170,y=9)
    print(dato.get())

def conectar(adress):
    port = 19999
    try:
        clientSocket.connect((adress,port))
        messagebox.showinfo("Mensaje Servido","Cliente conectado al robot: {0} : {1}".format(adress,port))
    except socket.error:
        messagebox.showwarning("Conexión erronea","No se ha logrado al conexíon, verifique la Ip {0}".format(adress))
        getAddres()
        clientSocket.close()




#ETIQUETAS

img2 = tk.PhotoImage(file="gorilla.png")
lnl_img2 = tk.Label(ventana,image = img2, bg = "gray25").place(x=80,y=0)


#Angulo
img3 = tk.PhotoImage(file="Angulo.png")
lnl_img3 = tk.Label(ventana,image = img3,bg = "gray25").place(x=600,y=100)
opcion=StringVar()
angulo = Spinbox(ventana,state="readonly",values=("0","45"),textvariable=opcion).place(x=600,y=270)


boton_angulo = Button(ventana, text="Ingresar", command=Angulo,background = "gray25",fg="white",font=("Arial Black",10)).place(x=600, y=300)


#Botones
#Boton Detener
img4 = tk.PhotoImage(file="ONOFF.png")
boton_salir = Button(ventana,image=img4, command=ventana.destroy,bg = "gray25").place(x=600, y=390)

#Boton Arriba
img_boton_arri = tk.PhotoImage(file="Arriba.png")
boton_arriba = tk.Button(repeatdelay=50,repeatinterval=50,image=img_boton_arri,command=Arriba, background = "gray25")
boton_arriba.place(x=170, y=340)
boton_arriba.bind('<ButtonRelease-1>',on_realese)
#Boton Abajo
img_boton_abaj = tk.PhotoImage(file="Abajo.png")
boton_abajo = tk.Button(repeatdelay=50,repeatinterval=50,image=img_boton_abaj,command=Abajo, background = "gray25")
boton_abajo.place(x=170, y=450)
boton_abajo.bind('<ButtonRelease-1>',on_realese)
#Boton Izquierda
img_boton_izq = tk.PhotoImage(file="Izquierda.png")
boton_izq = tk.Button(repeatdelay=50,repeatinterval=50,image=img_boton_izq,command=Izquierda, background = "gray25")
boton_izq.place(x=60, y=400)
boton_izq.bind('<ButtonRelease-1>',on_realese)
#Boton Derecha
img_boton_derech = tk.PhotoImage(file="Derecha.png")
boton_derech = tk.Button(repeatdelay=50,repeatinterval=50,image=img_boton_derech,command=Derecha, background = "gray25")
boton_derech.place(x=280, y=400)
boton_derech.bind('<ButtonRelease-1>',on_realese)
#Boton Disparar
boton_disparar = tk.Button(repeatdelay =50,repeatinterval = 50,text="Disparar 🎯",command=Disparar, background = "gray25",fg="white",font=("Arial Black",10))
boton_disparar.place(x=175,y=600)
boton_disparar.bind('<ButtonRelease-1>',Cannon)

#Boton Conectar
button_connect = tk.Button(ventana,text = "Conectar 📡",command=getAddres,bg = "gray25",fg="white",font=("Arial Black",10)).place(x=600,y=550)
#Boton Distancia
button_distancia = tk.Button(ventana,text = "Distancia 📏",command= Distancia ,bg = "gray25",fg="white",font=("Arial Black",10)).place(x=280,y=355)


#Boton Sonido
button_sonido =tk.Button(ventana,text = "GorillaTank 🤖",command=Luciano,bg = "gray25",fg="white",font=("Arial Black",10)).place(x=10,y=355)
clientSocket = socket.socket()
port = 1999
ipAddress = "192.168.201.160"



ventana.mainloop()



