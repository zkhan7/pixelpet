import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/firebase")
import firebase_interface as firebase
from time import sleep

from sense_hat import SenseHat
sense = SenseHat()

blue = (0, 0, 255)
magenta = (255, 0, 255)


def write_test_data1():
    # Write test data to the Firebase Realtime Database
    test_data = {
        "Feedings": 4,
        "Temperature": 41.10126495361328,
        "PetClean": 1,
        "Steps": 26,
        "LitterClean": 1
    }
    for key, value in test_data.items():
        firebase.write_database(key, value)

def write_test_data2():
    # Write test data to the Firebase Realtime Database
    test_data = {
        "Feedings": 4,
        "Temperature": 41.10126495361328,
        "PetClean": 0,
        "Steps": 26,
        "LitterClean": 1
    }
    for key, value in test_data.items():
        firebase.write_database(key, value)

def calculate_mood_score(feedings_data, temperature_data, pet_clean_data, steps_data, litter_clean_data):
    # Calculate mood score based on provided structure
    mood_score = (feedings_data * 0.4) + (temperature_data * 0.2) + (pet_clean_data * 0.1) + (steps_data * 0.2) + (litter_clean_data * 0.1)
    return min(100, max(0, mood_score*100))  # Ensure mood score is between 0 and 100

def display_mood_score(mood_score):
    # Display mood score on SenseHat
    message = "Mood Score: {}".format(round(mood_score, 1))
    sense.show_message(message, text_colour=magenta, back_colour=blue, scroll_speed=0.05)

def run_test_cases():
        
        # Write test data
        print("Test 1 begin")
        write_test_data1()
        # Read test data from the database
        feedings = firebase.read_database("Feedings")
        if (feedings == 4):
            feedings_data =1
        else:
            feedings_data = 0  
        temperature = firebase.read_database("Temperature")
        if (temperature >10):
            temperature_data = 1
        else:
            temperature_data = 0  
        pet_clean = firebase.read_database("PetClean")
        if (pet_clean == 1):
            pet_clean_data = 1
        else:
            pet_clean_data = 0  
        steps = firebase.read_database("Steps")
        if (steps>= 25):
            steps_data = 1
        else:
            steps_data = 0     
        litter_clean = firebase.read_database("LitterClean")
        if (litter_clean == 1):
            litter_clean_data = 1
        else:
            litter_clean_data = 0
        
        # Calculate mood score
        mood_score = calculate_mood_score(feedings_data, temperature_data, pet_clean_data, steps_data, litter_clean_data)
        print(f"Calculated Mood Score: {mood_score}")
        # Check if the calculated mood score matches the expected mood score
        if mood_score == 100:
            print("Test Case 1 passed!")
            firebase.write_database("MoodScore", mood_score)
            display_mood_score(mood_score)
        else:
            print(f"Test Case {test_number} failed! Expected: {expected_mood_score}, Actual: {mood_score}")
        print("Test 2 begin")
        write_test_data2()
    # Read test data from the database
        feedings = firebase.read_database("Feedings")
        if (feedings == 4):
            feedings_data =1
        else:
            feedings_data = 0  
        temperature = firebase.read_database("Temperature")
        if (temperature >10):
            temperature_data = 1
        else:
            temperature_data = 0  
        pet_clean = firebase.read_database("PetClean")
        if (pet_clean == 1):
            pet_clean_data = 1
        else:
            pet_clean_data = 0  
        steps = firebase.read_database("Steps")
        if (steps>= 25):
            steps_data = 1
        else:
            steps_data = 0     
        litter_clean = firebase.read_database("LitterClean")
        if (litter_clean == 1):
            litter_clean_data = 1
        else:
            litter_clean_data = 0
        
        # Calculate mood score
        mood_score = calculate_mood_score(feedings_data, temperature_data, pet_clean_data, steps_data, litter_clean_data)
        print(f"Calculated Mood Score: {mood_score}")
        # Check if the calculated mood score matches the expected mood score
        if mood_score == 90:
            print("Test Case 2 passed!")
            firebase.write_database("MoodScore", mood_score)
            display_mood_score(mood_score)
        else:
            print(f"Test Case {test_number} failed! Expected: {expected_mood_score}, Actual: {mood_score}")


if __name__ == "__main__":
    run_test_cases()

