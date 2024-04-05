import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/firebase")
import firebase_interface as firebase
from time import sleep


firebase.write_database("MoodScore", 4)
while (True):
    sleep(10)
    temp = firebase.read_database("Temperature")
    if temp == 36:
        print("First test case passed!")
        print("Received a new entry of temperature")
        firebase.write_database("MoodScore", 5)
        break

while (True):
    sleep(10)
    temp = firebase.read_database("Temperature")
    if temp == -10:
        print("Second test case passed!")
        print("Received a new entry of temperature")
        firebase.write_database("MoodScore", 4)
        break
