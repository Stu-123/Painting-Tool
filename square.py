class Square:
    """
    A square can be defined by the user by providing x, y coordinates and the length of the square.
    A colour should also be provided.
    The draw() method can be called on the square object and provided with a canvas upon which to draw
    the square.
    """

    def __init__(self, x, y, length, colour):
        self.x = x
        self.y = y
        self.length = length
        self.colour = colour

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.length, self.y: self.y + self.length] = self.colour
