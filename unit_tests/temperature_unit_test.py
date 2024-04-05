import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/firebase")
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/temperature_rpi")
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/sms_module")


import firebase_interface as firebase
import temperature_led
import sms 
import temperature_led
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()
temp = round(sense.get_temperature(),1)
firebase.write_database("Temperature",temp)
print("Temperature data:", temp,"°C")
temperature_led.set_led(temp) # indicate temperature on LED
sms.sendSMS("Temperature",temp)
sleep(5)
temp = -10
firebase.write_database("Temperature",temp)
temperature_led.set_led(temp)
sms.sendSMS("Temperature",temp)
