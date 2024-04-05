# Author: Zakariya Khan 101186641
import board
import busio
import digitalio
import adafruit_sharpmemorydisplay

class Lcd:
    def __init__(self):
        """
        Initialize the LCD display object.

        This class uses the Adafruit Sharp Memory Display to show images on an LCD screen.

        It sets up the SPI communication and creates a Sharp Memory Display object.

        """
        spi = busio.SPI(board.SCK, MOSI=board.MOSI)
        scs = digitalio.DigitalInOut(board.D6)  # inverted chip select

        # Create Sharp Memory Display object
        self.display = adafruit_sharpmemorydisplay.SharpMemoryDisplay(spi, scs, 144, 168)

    def display_image(self, image):
        """
        Display an image on the LCD screen.

        This method resizes the image to match the display dimensions, clears the display,
        shows the resized image on the display, and updates the display.

        Parameters:
        - image (PIL.Image.Image): The image to display on the LCD screen.

        """
        # Resize image to match display dimensions
        image = image.resize((self.display.width, self.display.height))

        # Clear display
        self.display.fill(1)
        self.display.show()
        # Show image
        self.display.image(image)
        self.display.show()


