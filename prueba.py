#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedRPM, MoveTank
import math
import os
import sys

mPalo = LargeMotor(OUTPUT_B)
distancia = 1
pi = math.pi
angulo = (5*pi)/36
degree = 25
tiempo = math.sqrt((0.08+math.tan(angulo)*distancia)/(4.9))
vel_necesaria = distancia/(math.cos(angulo)*tiempo)    
vel_rpm = (60*vel_necesaria)/(2*pi*0.189)
    # Rotar el motor en -180 grados al 6% de velocidad
mPalo.on_for_degrees(6,-300)
    # Rotar el motor en 225 grados al porcentaje de velocidad de vel_rpm
mPalo.on_for_degrees(SpeedRPM(round(vel_rpm)),300+degree)
    # Rotar el motor en -45 grados al 6% de la velocidad
mPalo.on_for_degrees(6,-degree)

