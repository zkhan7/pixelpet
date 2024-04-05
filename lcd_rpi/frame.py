# Author: Zakariya Khan 101186641
from PIL import Image

# Colors
BLACK = 0
WHITE = 255

class Frame:
    def __init__(self, width, height):
        """
        Initialize a frame with the specified width and height.

        Parameters:
        - width (int): The width of the frame in pixels.
        - height (int): The height of the frame in pixels.
        """
        self.width = width
        self.height = height
        self.frame = Image.new("1", (width, height), color=WHITE)

    def get_image(self):
        """
        Get the current frame as a PIL.Image.Image object.

        Returns:
        - frame (PIL.Image.Image): The current frame image.
        """
        return self.frame

    def overlay(self, image):
        """
        Overlay the given image on the current frame.

        Parameters:
        - image (PIL.Image.Image): The image to overlay on the frame.
        """
        # convert the current frame and images to pixels
        frame_pixles = list(self.frame.getdata())
        image_pixles = list(image.getdata())
        
        overlay_pixels = [BLACK if (frame_pixles[i] == BLACK or image_pixles[i] == BLACK) else WHITE  for i in range(len(frame_pixles))]
        res_image = Image.new("1", (self.width, self.height), color=0)
        # Update the image with the modified pixels
        res_image.putdata(overlay_pixels)
        self.frame = res_image

    def clear(self):
        """Clear the frame, resetting it to a blank white image."""
        self.frame = Image.new("1", (self.width, self.height), color=WHITE)