import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/firebase")
from sense_hat import SenseHat
import time
import math
import firebase_interface as firebase

# Initialize Sense HAT
sense = SenseHat()

# Constants
STEP_THRESHOLD = 1.2
steps = 0

# Main loop
try:
    while steps<5:
        # Read accelerometer data
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']
        
        # Calculate magnitude
        magnitude = math.sqrt(x**2 + y**2 + z**2)
        
        # Check for steps
        if magnitude > STEP_THRESHOLD:
            steps += 1
            sense.show_message("{}".format(steps))  # Display step count
            print("Step detected! Total steps:", steps)
            time.sleep(0.2)  # Add a small delay to prevent multiple steps being counted

    
    firebase.write_database("Steps",steps)
    assert(firebase.read_database("Steps") == 5)

except KeyboardInterrupt:
    sense.clear()
    print("\nExiting...")
