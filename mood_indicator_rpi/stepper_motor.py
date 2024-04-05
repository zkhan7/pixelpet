#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/firebase")
import firebase_interface as firebase

in1 = 18
in2 = 23
in3 = 24
in4 = 25

currPosition = 50

step_sleep = 0.002

# 4096 steps for 360 degrees, so steps_per_degree = 4096 / 180
steps_per_degree = 4096 / 180

direction = False  # True for clockwise, False for counter-clockwise

# defining stepper motor sequence
step_sequence = [[1, 0, 0, 1],
                 [1, 0, 0, 0],
                 [1, 1, 0, 0],
                 [0, 1, 0, 0],
                 [0, 1, 1, 0],
                 [0, 0, 1, 0],
                 [0, 0, 1, 1],
                 [0, 0, 0, 1]]

GPIO.setwarnings(False)

# setting up
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

# initializing
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)

motor_pins = [in1, in2, in3, in4]
motor_step_counter = 0

def move_stepper_motor(newPosition):
    global motor_step_counter, currPosition  # Declare motor_step_counter as a global variable

    #to set range from 0-90 degrees
    newPosition = newPosition/2

    #move to new position based on previous
    position = newPosition - currPosition

    if (position < 0):
        direction = True
    else:
        direction = False

    steps_to_move = int(steps_per_degree * abs(position))
    for _ in range(steps_to_move):
        for pin in range(0, len(motor_pins)):
            GPIO.output(motor_pins[pin], step_sequence[motor_step_counter][pin])
        if direction:
            motor_step_counter = (motor_step_counter - 1) % 8
        else:
            motor_step_counter = (motor_step_counter + 1) % 8
        time.sleep(step_sleep)

    currPosition = newPosition
