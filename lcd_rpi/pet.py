# Author: Zakariya Khan 101186641
import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/firebase")
import firebase_interface as firebase
import threading
from time import sleep

POOP_TIME = 20
HUNGER_TIME = 30
class Pet:
    """
    A class representing a virtual pet.

    Attributes:
    - __mood (str): The mood of the pet (can be "happy", "neutral", or "sad").
    - __interaction (str): The current interaction of the pet (e.g., "feeding", "play", "litter_clean", "pet_clean").
    - __litter (bool): Flag indicating whether the pet has litter.
    - __feedings (int): Number of feedings the pet has received.
    - __poop (threading.Thread): Thread for managing the poop timer.

    Methods:
    - __init__(self): Constructor to initialize the pet with default values and start threads for hunger and poop timers.
    - hunger(self): Method to handle hunger logic and decrease feedings over time.
    - get_mood(self): Method to get the current mood of the pet.
    - get_interaction(self): Method to get the current interaction of the pet.
    - clear_interaction(self): Method to clear the current interaction of the pet.
    - is_interaction(self): Method to check if the pet is currently interacting.
    - clean(self): Method to handle cleaning interactions based on the pet's state and update the database accordingly.
    - is_litter(self): Method to check if the pet has litter.
    - poop(self): Method to handle the poop timer and update the database when the pet poops.
    - feed(self): Method to handle feeding interactions, increase feedings, start the poop timer, and update the database.
    - play(self): Method to handle play interactions based on the pet's mood and current interaction state.
    - set_mood(self, mood_score): Method to set the mood of the pet based on a mood score from the database.
    """
     
    def __init__(self):
        """
        Initialize the pet with default values and start threads for hunger and poop timers.
        """
        self.__mood = "neutral"
        self.__interaction = None
        self.__litter = False
        self.__feedings = 1
        threading.Thread(target=self.hunger, name="hunger").start()
        self.__poop = threading.Thread(target=self.poop, name="poop_timer")

    def hunger(self):
        """
        Handle hunger logic and decrease feedings over time.
        """
        while True:
            sleep(HUNGER_TIME)
            if self.__feedings > 0:
                self.__feedings -= 1
                firebase.write_database("Feedings", self.__feedings)

    def get_mood(self):
        """
        Get the current mood of the pet.

        Returns:
        - str: The current mood of the pet ("happy", "neutral", or "sad").
        """
        return self.__mood
    
    def get_interaction(self):
        """
        Get the current interaction of the pet.

        Returns:
        - str: The current interaction of the pet.
        """
        return self.__interaction
    
    def clear_interaction(self):
        """
        Clear the current interaction of the pet.
        """
        self.__interaction = None
    
    def is_interaction(self):
        """
        Check if the pet is currently interacting.

        Returns:
        - bool: True if the pet is interacting, False otherwise.
        """
        if self.__interaction is not None:
            return True
        return False
    
    def clean(self):
        """
        Handle cleaning interactions based on the pet's state and update the database accordingly.
        """
        if self.__interaction is None:
            if self.__litter:
                self.__interaction = "litter_clean"
                self.__litter = False
                firebase.write_database("LitterClean", 1)
            else:
                self.__interaction = "pet_clean"
                firebase.write_database("PetClean", 1)
              
              
    def is_litter(self):
        """
        Check if the pet has litter.

        Returns:
        - bool: True if the pet has litter, False otherwise.
        """
        return self.__litter
    
    def poop(self):
        """
        Handle the poop timer and update the database when the pet poops.
        """
        # write 0 for litter_clean in the database
        sleep(POOP_TIME)
        firebase.write_database("LitterClean", 0)
        self.__litter = True
    
    def feed(self):
        """
        Handle feeding interactions, increase feedings, start the poop timer, and update the database.

        Returns:
        - bool: True if the pet is successfully fed, False otherwise.
        """
        if self.__interaction is None:
            self.__interaction = "feeding"
            if self.__feedings < 4:
                self.__feedings += 1
                print(self.__feedings)
                firebase.write_database("Feedings", self.__feedings)
            if (not self.__poop.is_alive()):
                self.__poop = threading.Thread(target=self.poop, name="poop_timer")
                self.__poop.start()
            return True
    
    def play(self):
        """
        Handle play interactions based on the pet's mood and current interaction state.
        """
        if self.__interaction == None and self.__mood == "happy":
                self.__interaction = "play"
    
    def set_mood(self, mood_score):
        """
        Set the mood of the pet based on a mood score from the database.

        Parameters:
        - mood_score (int): The mood score from the database.
        """
        if mood_score <= 34:
            self.__mood = "sad"
        elif mood_score <= 66:
            self.__mood = "neutral"
        else:
            self.__mood = "happy"

                    