# Author: Zakariya Khan 101186641
from gpiozero import Button
from time import sleep
import threading
import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/firebase")
import firebase_interface as firebase

feed_button = Button(17)
clean_button = Button(27)
play_button = Button(22)

DIRTY_INTERVAL = 300
READ_MOOD_INTERVAL = 3

def feed_listen(pet):
    """
    Listen for button presses and feed the pet when the feed button is pressed.

    Parameters:
    - pet (Pet): The pet object to feed.
    """
    while True:
        feed_button.wait_for_press()
        pet.feed()
        sleep(0.5) # debounce time

def clean_listen(pet):
    """
    Listen for button presses and clean the pet when the clean button is pressed.

    If the clean button is held down for DIRTY_INTERVAL seconds, clean the pet;
    otherwise, update the database with the pet's cleanliness status.

    Parameters:
    - pet (Pet): The pet object to clean.
    """
    while True:
        clean_button.wait_for_press(DIRTY_INTERVAL)
        if clean_button.is_pressed:
            pet.clean()
            sleep(0.5)
        else:
            firebase.write_database("PetClean", 0)

def play_listen(pet):
    """
    Listen for button presses and play with the pet when the play button is pressed.

    Parameters:
    - pet (Pet): The pet object to play with.
    """
    while True:
        play_button.wait_for_press()
        pet.play()
        sleep(0.5)

def mood_listen(pet):
    """
    Listen for mood updates from the database and update the pet's mood accordingly.

    Parameters:
    - pet (Pet): The pet object to update the mood for.
    """
    while True:
        pet.set_mood(firebase.read_database("MoodScore"))
        sleep(READ_MOOD_INTERVAL)

def start_threads(pet):
    """
    Start listener threads for button presses and mood updates.

    Parameters:
    - pet (Pet): The pet object to interact with.
    """
    # Create multiple threads
    feed_button_listener = threading.Thread(target=feed_listen, args=(pet,), name="feed_button listener")
    clean_button_listener = threading.Thread(target=clean_listen, args=(pet,), name="clean_button listener")
    play_button_listener = threading.Thread(target=play_listen, args=(pet,), name="play_button listener")
    mood_listener = threading.Thread(target=mood_listen, args=(pet,), name="mood listener")
    
    # Start the threads
    feed_button_listener.start()
    clean_button_listener.start()
    play_button_listener.start()
    mood_listener.start()

