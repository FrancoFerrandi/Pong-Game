from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.setposition(x, y)

    def up(self):
        if self.ycor() != 240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() != -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
