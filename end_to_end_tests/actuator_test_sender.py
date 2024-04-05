import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/firebase")
import firebase_interface as firebase
from time import sleep

print("Sending Mood Score data: 50")
firebase.write_database("MoodScore", 50)
while (True):
    sleep(10)
    mood = firebase.read_database("MoodScore")
    if mood == 1:
        print("First test case passed!")
        break

print("Sending Mood Score data: 100")
firebase.write_database("MoodScore", 100)
while (True):
    sleep(10)
    mood = firebase.read_database("MoodScore")
    if mood == 2:
        print("Second test case passed!")
        break

