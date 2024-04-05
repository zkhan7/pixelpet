import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/firebase")
import firebase_interface as firebase
from time import sleep

print("Sending Step data: 40 steps")
firebase.write_database("Steps", 40)
while (True):
    sleep(10)
    mood = firebase.read_database("MoodScore")
    if mood == 8:
        print("First test case passed!")
        print("Received back corresponding mood from actuator rpi. \n Mood based on steps", mood, "(40 steps * 0.2)")
        break

print("Sending Step data: 80 steps")
firebase.write_database("Steps",80)
while (True):
    sleep(10)
    mood = firebase.read_database("MoodScore")
    if mood == 24:
        print("Second test case passed!")
        print("Received back corresponding mood from actuator rpi. \n Mood based on steps: 24", mood)
        break
