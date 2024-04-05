from sense_hat import SenseHat
import threading
import math
import time
import os
import sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/firebase")
import firebase_interface as firebase


class Pedometer:
    def __init__(self):
        #start at 90 to be able to increment right away
        self.steps = 90
        self.STEP_THRESHOLD = 1.2
        self.sense = SenseHat()

        #thread for step increment
        threading.Thread(target=self.step_counter, daemon=True).start()

        #thread for step decrement
        threading.Thread(target=self.step_decrementer, daemon=True).start()

    """"
    When a step is registered if the total is less than 100 it will increment the total and push to firebase
    """
    def step_counter(self):
        while True:
            acceleration = self.sense.get_accelerometer_raw()
            x = acceleration['x']
            y = acceleration['y']
            z = acceleration['z']
            magnitude = math.sqrt(x ** 2 + y ** 2 + z ** 2)
            if magnitude > self.STEP_THRESHOLD:
                print("STEP TAKEN")
                if self.steps < 100:
                    self.steps += 1
                    self.update_database()

    """"
    Every 30 seconds the step counter is decremented to show the pet needs more steps to stay happy
    """
    def step_decrementer(self):
        while True:
            time.sleep(30)  # Decrease steps every 30 seconds
            if self.steps > 0:
                self.steps -= 1
                self.update_database()
                self.sense.show_message("{}".format(self.steps))  # Display step count


    def update_database(self):
        firebase.write_database("Steps", self.steps)

if __name__ == "__main__":
    pedometer = Pedometer()
    while True:
        pedometer.sense.show_message("{}".format(pedometer.steps))  # Display step count
        time.sleep(1)  # Keep the main thread alive
