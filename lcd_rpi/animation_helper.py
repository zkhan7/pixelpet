# Author: Zakariya Khan 101186641
from PIL import Image
import os

# Colors
BLACK = 0
WHITE = 255

# Dimensions
WIDTH = 144
HEIGHT = 168

def load_image(image_path):
    """
    Load an image from the specified path and resize it to match the display dimensions.

    Parameters:
    - image_path (str): The path to the image file.

    Returns:
    - image (PIL.Image.Image): The loaded and resized image.
    """
    # Load image
    image = Image.open(image_path).convert("1")

    # Resize image to match display dimensions
    image = image.resize((WIDTH, HEIGHT))

    return image

def get_child_images(directory_in_str):
    """
    Get all images from the specified directory with supported file extensions.

    Parameters:
    - directory_in_str (str): The path to the directory containing images.

    Returns:
    - files (list): A list of PIL.Image.Image objects representing the loaded images.
    """
    directory = os.fsencode(directory_in_str)
    files = []
    for file in sorted(os.listdir(directory)):
        filename = os.fsdecode(file)
        if filename.endswith(".png") or filename.endswith(".jpg"): 
            files.append(load_image(str(directory_in_str+"/"+filename)))
        else:
            continue
    return files

def get_animation_dict(path):
    """
    Create a dictionary of animations from subdirectories in the specified path.

    Parameters:
    - path (str): The base directory containing subdirectories with animation images.

    Returns:
    - animations (dict): A dictionary mapping animation names to lists of image objects.
    """
    animations = {
        "UI" : load_image(str(path+"UI.png")),
        "startup" : load_image(str(path+"startup.png")),
        "pet_base" : get_child_images(str(path+"pet_base")),
        "moods" : get_child_images(str(path+"moods")),
        "feeding" : get_child_images(str(path+"feeding")), 
        "pet_clean" : get_child_images(str(path+"pet_clean")),
        "play" : get_child_images(str(path+"play")),
        "poop" : get_child_images(str(path+"poop")),
        "litter_clean" : get_child_images(str(path+"litter_clean"))
    }
    return animations

