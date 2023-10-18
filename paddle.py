from turtle import Turtle
"""Create a paddle object and move it to a particular location specified"""

class Paddle(Turtle):  # Renamed the class to 'Paddle' (capitalized)
    def __init__(self, x_pos, y_pos):
        """Ensure i dont overide the original turtle class"""
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.shape('square')
        self.color('white')
        self.penup()
        self.turtlesize(0.5, 4)
        self.setheading(90)
        self.goto(x_pos, y_pos)
        self.move_distance = 10

    
    def move_up(self):
        """Moves the paddle Up"""
        self.forward(self.move_distance)

    def move_down(self):
        """Moves the paddle Down"""
        self.backward(self.move_distance)
