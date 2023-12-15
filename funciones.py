#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedRPM, MoveTank
from ev3dev2.sound import Sound
import math
import os
import sys

os.system('setfont Lat15-TerminusBold14')

#movimiento simultaneo de las ruedas(rueda izquierda, rueda derecha)
movimiento_ruedas = MoveTank(OUTPUT_A, OUTPUT_D)
#movimiento del palo del robot
mPalo = LargeMotor(OUTPUT_B)
#movimiento de rotacion de las ruedas delanteras
mRotar = MediumMotor(OUTPUT_C)


#funcion para lanzar un objeto con el palo
def lanzar(distancia):
    pi = math.pi
    vel_necesaria = math.sqrt((4.9*distancia)/math.cos(pi/4)*math.sin(pi/4))
    vel_rpm = (60*vel_necesaria)/(2*pi*0.189)
    if vel_rpm < 175 and vel_rpm > 0:
        # Rotar el motor en -180 grados al 6% de velocidad
        mPalo.on_for_degrees(6,-180)
        # Rotar el motor en 225 grados al porcentaje de velocidad de vel_rpm
        mPalo.on_for_degrees(SpeedRPM(round(vel_rpm)),225)
        # Rotar el motor en -45 grados al 6% de la velocidad
        mPalo.on_for_degrees(6,-45)

#funcion para mover el robot hacia adelante
def mover_adelante():
    movimiento_ruedas.on(-100, -100)

#funcion para mover el robot hacia atras
def mover_atras():
    movimiento_ruedas.on(100, 100)

#funcion para mover el robot hacia la izquierda
def mover_izquierda():
    mRotar.on_for_degrees(30, 25)
    movimiento_ruedas.on(100, -100)

#funcion para mover el robot hacia la derecha
def mover_derecha():
    mRotar.on_for_degrees(-30, 25)
    movimiento_ruedas.on(-100, 100)

#funcion para detener el robot
def detener():
    movimiento_ruedas.stop()
