import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/firebase")
import firebase_interface as firebase
import temperature_led
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()
TEMPERATURE_OFFSET = 13
PERIOD = 10 # TODO change this period later
while(True):
    # Testing readData function
    temp = sense.get_temperature() - TEMPERATURE_OFFSET
    print("Temperature data:", temp,"°C")
    temperature_led.set_led(temp) # indicate temperature on LED
    # Testing writeData function
    print("Writing Temperature data to Firebase:")
    firebase.write_database("Temperature",temp)
    sleep(PERIOD)

