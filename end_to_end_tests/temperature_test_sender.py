import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/firebase")
import firebase_interface as firebase
from time import sleep

print("Sending temperature data: 36 C")
firebase.write_database("Temperature", 36)
while (True):
    sleep(10)
    mood = firebase.read_database("MoodScore")
    if mood == 5:
        print("First test case passed!")
        print("Received back corresponding mood from actuator rpi. \n Mood based on temperature: ", mood)
        break

print("Sending temperature data:  -10 C")
firebase.write_database("Temperature",-10)
while (True):
    sleep(10)
    mood = firebase.read_database("MoodScore")
    if mood == 4:
        print("Second test case passed!")
        print("Received back corresponding mood from actuator rpi. \n Mood based on temperature: ", mood)
        break

