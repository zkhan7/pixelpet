from gpiozero import Button
from time import sleep
import threading

feed_button = Button(17)
clean_button = Button(27)
play_button = Button(22)
fed = False
# Define a function to be executed by the listener threads
def feed_listen():
    while True:
        feed_button.wait_for_press()
        print("Feeding pet")
        sleep(0.5)
        fed = True
        timer = threading.Thread(target=count_down, name="timer")
        timer.start()
        while (timer.is_alive()):
            feed_button.wait_for_press()
            print("Pet was already fed")
            sleep(0.5)

def clean_listen():
    while True:
        clean_button.wait_for_press()
        print("Cleaning pet")
        sleep(0.5)

def play_listen():
    while True:
        play_button.wait_for_press()
        print("playing with pet")
        sleep(0.5)

def count_down():
    sleep(10)
# Create multiple threads
feed_button_listener = threading.Thread(target=feed_listen, name="feed_button listener")
clean_button_listener = threading.Thread(target=clean_listen, name="clean_button listener")
play_button_listener = threading.Thread(target=play_listen, name="play_button listener")

# Start the threads
feed_button_listener.start()
clean_button_listener.start()
play_button_listener.start()

