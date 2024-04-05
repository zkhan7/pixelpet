import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/firebase")
import firebase_interface as firebase
from time import sleep
from sense_hat import SenseHat
import RPi.GPIO as GPIO
import time

PERIOD = 10 # Shortended for demo purposes
TEMPERATURE_OFFSET = 13
TEMP_FACTOR = 0.1
STEP_FACTOR = 0.2
FEEDING_FACTOR = 0.4
PET_CLEAN_FACTOR = 0.2
LITTER_CLEAN_FACTOR = 0.1

IN1 = 18
IN2 = 23
IN3 = 24
IN4 = 25

curr_position = 50
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
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# initializing
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)
GPIO.output(IN3, GPIO.LOW)
GPIO.output(IN4, GPIO.LOW)

motor_pins = [IN1, IN2, IN3, IN4]
motor_step_counter = 0

"""Moves Stepper motor based on input position."""


def move_stepper_motor(newPosition: int):
    # Declare as global to keep track of previous position
    global motor_step_counter, curr_position

    # To set max to 90 degrees divide position by 2
    newPosition = newPosition/2

    # move to new position based on previous
    position = newPosition - curr_position

    if (position < 0):
        direction = True
    else:
        direction = False

    steps_to_move = int(steps_per_degree * abs(position))
    for _ in range(steps_to_move):
        for pin in range(0, len(motor_pins)):
            GPIO.output(motor_pins[pin],
                        step_sequence[motor_step_counter][pin])
        if direction:
            motor_step_counter = (motor_step_counter - 1) % 8
        else:
            motor_step_counter = (motor_step_counter + 1) % 8
        time.sleep(step_sleep)

    curr_position = newPosition


"""Calculates overall mood of pet."""


def calculate_mood(temp: int, steps: int, feeding: int,
                   pet_clean: int, litter_clean: int) -> int:
    # each score is out of 100
    temp_score = 0
    steps_score = 0
    feeding_score = 0
    pet_clean_score = 0
    litter_clean_score = 0

    if temp is not None:
        if 18 <= temp <= 24:
            temp_score = 100
        elif 10 <= temp <= 17 or 24 <= temp <= 28:
            temp_score = 50

    if steps is not None:
        if steps >= 100:
            steps_score = 100
        else:
            steps_score = steps

    if feeding is not None:
        if (feeding >= 4):
            feeding_score = 100
        elif (feeding == 3):
            feeding_score = 75
        elif (feeding == 2):
            feeding_score = 50
        elif (feeding == 1):
            feeding_score = 25

    if pet_clean is not None:
        if pet_clean == 1:
            pet_clean_score = 100

    if litter_clean is not None:
        if litter_clean == 1:
            litter_clean_score = 100

    return (
        temp_score * TEMP_FACTOR +
        steps_score * STEP_FACTOR +
        feeding_score * FEEDING_FACTOR +
        pet_clean_score * PET_CLEAN_FACTOR +
        litter_clean_score * LITTER_CLEAN_FACTOR
    )


move_stepper_motor(curr_position)

# main loop that collects data
while (True):
    # Get data from database
    temperature_data = firebase.read_database("Temperature") - TEMPERATURE_OFFSET

    steps_data = firebase.read_database("Steps")

    feedings_data = firebase.read_database("Feedings")

    pet_clean_data = firebase.read_database("LitterClean")

    litter_clean_data = firebase.read_database("PetClean")

    # calculate the mood given the data
    mood = calculate_mood(temp=temperature_data, steps=steps_data, feeding=feedings_data, pet_clean=pet_clean_data, litter_clean=litter_clean_data)
    
    move_stepper_motor(mood)

    firebase.write_database("MoodScore", mood)

    sleep(PERIOD)
