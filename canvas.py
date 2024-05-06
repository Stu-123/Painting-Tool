import numpy as np
from PIL import Image


class Canvas:
    """
    A canvas is an object upon which rectangle and square objects can be rendered.
    """

    def __init__(self, colour=(255, 255, 255), width=100, height=100):
        self.width = width
        self.height = height
        self.colour = colour

        # Create a 3D array of zeros using numpy
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)

        # Update the zeros array using the user given values for canvas colour
        self.data[:] = self.colour

    def make(self, image_path):
        """
        Converts the canvas array into an image file.

        """
        img = Image.fromarray(self.data, 'RGB')
        img.save(image_path)
