import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/firebase")
import firebase_interface as firebase
from time import sleep

print("Sending Feedings data: 4 back to back feedings")
firebase.write_database("Feedings", 1)
firebase.write_database("Feedings", 1)
firebase.write_database("Feedings", 1)
firebase.write_database("Feedings", 1)
while (True):
    sleep(10)
    mood = firebase.read_database("MoodScore")
    if mood == 40:
        print("First test case passed!")
        print("Received back corresponding mood from actuator rpi. \n Mood based on feedings", mood, "(100 * 0.4)")
        break

print("Sending Feedings data: 0 feedings 4 times")
firebase.write_database("Feedings", 0)
firebase.write_database("Feedings", 0)
firebase.write_database("Feedings", 0)
firebase.write_database("Feedings", 0)
while (True):
    sleep(10)
    mood = firebase.read_database("MoodScore")
    if mood == 0:
        print("Second test case passed!")
        print("Received back corresponding mood from actuator rpi. \n Mood based on Feedings: 0", mood)
        break
