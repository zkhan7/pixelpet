import board
import busio
import digitalio
from PIL import Image
import adafruit_sharpmemorydisplay
from time import sleep
import os


# Colors
BLACK = 0
WHITE = 255

spi = busio.SPI(board.SCK, MOSI=board.MOSI)
scs = digitalio.DigitalInOut(board.D6)  # inverted chip select

# Create Sharp Memory Display object
display = adafruit_sharpmemorydisplay.SharpMemoryDisplay(spi, scs, 144, 168)


def get_animation_dict():
    """
    Get a dictionary of animation frames from specified directories.
    """
    path = str(os.path.dirname(os.path.abspath(__file__)) +
               "/../lcd_rpi/animations/")
    animations = {
        "UI": load_image(str(path + "UI.png")),
        "pet_base": get_images(str(path + "pet_base")),
        "moods": get_images(str(path + "moods")),
        "feeding": get_images(str(path + "feeding")),
        "pet_clean": get_images(str(path + "pet_clean")),
        # "play" : get_images(str(abs_path+"play")),
        "poop": get_images(str(path + "poop")),
        "poop_clean": get_images(str(path + "poop_clean"))
    }
    return animations


def get_images(directory_in_str):
    """
    Given a directory, return all files in the directory
    that are PNG or JPG images.
    """
    directory = os.fsencode(directory_in_str)
    files = []
    for file in sorted(os.listdir(directory)):
        filename = os.fsdecode(file)
        if filename.endswith(".png") or filename.endswith(".jpg"):
            files.append(load_image(str(directory_in_str + "/" + filename)))
        else:
            continue
    return files


def overlay(image1, image2):
    """
    Overlay two images by combining their pixels.
    """
    image1_pixels = list(image1.getdata())
    image2_pixels = list(image2.getdata())

    overlay_pixels = [BLACK if (image1_pixels[i] == BLACK
                                or image2_pixels[i] == BLACK) else WHITE
                      for i in range(len(image1_pixels))]
    res_image = Image.new("1", (display.width, display.height), color=0)
    res_image.putdata(overlay_pixels)

    return res_image


def load_image(image_path):
    """
    Load and resize an image from the specified path.
    """
    image = Image.open(image_path).convert("1")
    image = image.resize((display.width, display.height))
    return image


def display_image(image):
    """
    Display an image on the Sharp Memory Display.
    """
    display.fill(1)
    display.show()
    display.image(image)
    display.show()


animations = get_animation_dict()
idx = 0
animation_idx = 0
action = "none"
mood = "none"
poop_enabled = False
frame = animations["UI"]

while True:
    if idx == 0:
        mood = "sad"
    if idx == 4:
        action = "feeding"
        mood = "happy"
    if idx == 10:
        poop_enabled = True
        mood = "mid"

    if poop_enabled:
        frame = overlay(frame, animations["poop"][idx % 2])

    if idx == 14:
        action = "poop_clean"
        mood = "happy"

    if idx == 19:
        action = "pet_clean"
        mood = "happy"

    if poop_enabled:
        frame = overlay(frame, animations["poop"][idx % 2])

    frame = overlay(frame, animations["pet_base"][idx % 2])

    # Overlay mood images based on current mood
    if mood == "happy":
        frame = overlay(frame, animations["moods"][0])
    elif mood == "sad":
        frame = overlay(frame, animations["moods"][1])

    # Overlay action images based on current action
    if action == "pet_clean":
        frame = overlay(frame, animations["pet_clean"][animation_idx])
        if animation_idx == len(animations["pet_clean"]) - 1:
            animation_idx = 0
            action = "none"
        else:
            animation_idx += 1
    elif action == "feeding":
        frame = overlay(frame, animations["feeding"][animation_idx])
        if animation_idx == len(animations["feeding"]) - 1:
            animation_idx = 0
            action = "none"
        else:
            animation_idx += 1
    elif action == "poop_clean":
        frame = overlay(frame, animations["poop_clean"][animation_idx])
        if animation_idx == len(animations["poop_clean"]) - 1:
            animation_idx = 0
            poop_enabled = False
            action = "none"
        else:
            animation_idx += 1

    display_image(frame)
    sleep(1)
    frame = animations["UI"]
    idx = (idx + 1) % 25
