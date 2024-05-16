import turtle
from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")

# no me funciona
    """def create_line(self):
        num = 1
        for n in range(-250, 250):
            num = turtle.turtles()
            num += 1
"""