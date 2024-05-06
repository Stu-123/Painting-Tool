from canvas import Canvas
from rectangle import Rectangle
from square import Square

# Create a white canvas
output_canvas = Canvas(colour=(255, 255, 255))

# Create some shapes and draw them on the canvas
rectangle_1 = Rectangle(x=10, y=6, height=20, width=35, colour=(100, 231, 50))
rectangle_1.draw(output_canvas)
rectangle_2 = Rectangle(x=5, y=60, height=50, width=30, colour=(80, 102, 120))
rectangle_2.draw(output_canvas)
square_1 = Square(x=40, y=32, length=40, colour=(10, 120, 250))
square_1.draw(output_canvas)

# Render and save the canvas
Canvas.make(output_canvas, "test.png")
