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
mRotar.stop_action = 'hold'
rotacion = 0


#funcion para lanzar un objeto con el palo
def lanzar(distancia):
    pi = math.pi
    angulo = (5*pi)/36
    degree = 25
    tiempo = math.sqrt((0.08+math.tan(angulo)*distancia)/(4.9))
    vel_necesaria = distancia/(math.cos(angulo)*tiempo)    
    vel_rpm = (60*vel_necesaria)/(2*pi*0.189)
    if vel_rpm < 175 and vel_rpm > 0:
        # Rotar el motor en -300 grados al 6% de velocidad
        mPalo.on_for_degrees(6,-300)
        # Rotar el motor en 325 grados al porcentaje de velocidad de vel_rpm
        mPalo.on_for_degrees(SpeedRPM(round(vel_rpm)),300+degree)
        # Rotar el motor en -25 grados al 6% de la velocidad
        mPalo.on_for_degrees(6,-degree)

#funcion para mover el robot hacia adelante
def mover_adelante():
    movimiento_ruedas.on(-100, -100)

#funcion para mover el robot hacia atras
def mover_atras():
    movimiento_ruedas.on(100, 100)

#funcion para rotar las ruedas hacia la izquierda
def mover_izquierda():
    global rotacion
    if rotacion == 0 or rotacion == 25:
        mRotar.on_for_degrees(30, 25)
        rotacion -= 25


#funcion para rotar las ruedas hacia la derecha
def mover_derecha():
    global rotacion
    if rotacion == 0 or rotacion == -25:
        mRotar.on_for_degrees(-30, 25)
        rotacion += 25

#funcion para detener el robot
def detener():
    movimiento_ruedas.stop()
