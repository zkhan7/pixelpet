# Author: Zakariya Khan 101186641
from animation_helper import get_animation_dict
from lcd import Lcd as LCD
from frame import Frame
from pet import Pet
from listeners import start_threads
import os
from time import sleep

# Define the path to the animations directory
path = str(os.path.dirname(os.path.abspath(__file__)) + "/../lcd_rpi/animations/")

# Get animations dictionary using the path
animations = get_animation_dict(path)

# Initialize LCD, Frame, and index variables
lcd = LCD()
frame = Frame(lcd.display.width, lcd.display.height)
base_idx = 0
action_idx = 0

# display startup screen
lcd.display_image(animations["startup"])

# wait for connect to wifi
sleep(15) 

# Create a Pet object and start listener threads
pet = Pet()
start_threads(pet)

# Main loop for displaying animations on the LCD
while True:
    # Overlay UI and pet base animations on the frame
    frame.overlay(animations["UI"])
    frame.overlay(animations["pet_base"][base_idx])

    # Overlay mood animations based on the pet's mood
    match pet.get_mood():
        case "happy":
            frame.overlay(animations["moods"][0])
        case "sad":
            frame.overlay(animations["moods"][1]) 

    # Overlay interaction animations based on pet interaction state
    if (pet.is_interaction()):
        interaction = pet.get_interaction()
        if interaction == "play":
             frame.clear()
             frame.overlay(animations["UI"])
        frame.overlay(animations[interaction][action_idx])
        action_idx +=1
        if(action_idx == len(animations[interaction])):
                action_idx = 0
                pet.clear_interaction()

    # Overlay poop animation if the pet is littered
    if (pet.is_litter()):
        frame.overlay(animations["poop"][base_idx])

    # Display the frame on the LCD and wait for 1 second
    lcd.display_image(frame.get_image())
    sleep(1)

    # Clear the frame and update base_idx for cycling through animations
    frame.clear()
    base_idx = (base_idx + 1) % 2