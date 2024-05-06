class Rectangle:
    """
    A rectangle can be defined by the user by providing x, y coordinates and the height/width of the rectangle.
    A colour should also be provided.
    The draw() method can be called on the rectangle object and provided with a canvas upon which to draw
    the rectangle.
    """

    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

    def draw(self, canvas):
        """
        Draws the rectangle onto the canvas object.
        """
        # Access the data attribute in the canvas, and update it using the rectangle's values.
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.colour
