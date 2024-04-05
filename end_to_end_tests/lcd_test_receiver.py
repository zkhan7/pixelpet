import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/firebase")
import firebase_interface as firebase
from time import sleep


while (True):
    sleep(10)
    feedings = firebase.read_database("Feedings")
    if feedings == 4:
        print("First test case passed!")
        print("Received 4 back to back feedings")
        firebase.write_database("MoodScore", 40)
        break

while (True):
    sleep(10)
    feedings = firebase.read_database("Feedings")
    if feedings == 0:
        print("Second test case passed!")
        print("Received 0 feedings")
        firebase.write_database("MoodScore", 0)
        break