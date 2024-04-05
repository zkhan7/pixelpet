import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/firebase")
import firebase_interface as firebase
from time import sleep

from sense_hat import SenseHat
sense = SenseHat()

blue = (0, 0, 255)
magenta = (255, 0, 255)


while (True):
    sleep(10)
    moodScore = firebase.read_database("MoodScore")
    if moodScore == 50:
        print("First test case passed!")
        print("Received a new entry of MoodScore 50")
        firebase.write_database("MoodScore", 1)
        sense.show_message("Mood Score 50", text_colour=magenta, back_colour=blue, scroll_speed=0.05)
        break

while (True):
    sleep(10)
    moodScore = firebase.read_database("MoodScore")
    if moodScore == 100:
        print("Second test case passed!")
        print("Received a new entry of MoodScore 100")
        firebase.write_database("MoodScore", 2)
        sense.show_message("Mood Score 100", text_colour=magenta, back_colour=blue, scroll_speed=0.05)
        break


