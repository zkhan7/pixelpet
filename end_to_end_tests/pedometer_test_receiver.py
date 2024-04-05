import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/firebase")
import firebase_interface as firebase
from time import sleep


while (True):
    sleep(10)
    steps = firebase.read_database("Steps")
    if steps == 40:
        print("First test case passed!")
        print("Received a new entry of 40 steps")
        firebase.write_database("MoodScore", 8)
        break

while (True):
    sleep(10)
    steps = firebase.read_database("Steps")
    if steps == 80:
        print("Second test case passed!")
        print("Received a new entry of 80 steps")
        firebase.write_database("MoodScore", 24)
        break