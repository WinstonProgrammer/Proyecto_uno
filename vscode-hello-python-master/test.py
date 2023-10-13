#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_2
from ev3dev2.sensor.lego import UltrasonicSensor
import os

os.system('setfont Lat15-TerminusBold14')

mL = LargeMotor(OUTPUT_A); mL.stop_action = 'hold'

mR = LargeMotor(OUTPUT_B); mR.stop_action = 'hold'

mL.run_to_rel_pos(position_sp= 840, speed_sp = 250)

mR.run_to_rel_pos(position_sp=-840, speed_sp = 250)

mL.wait_while('running')

mR.wait_while('running')