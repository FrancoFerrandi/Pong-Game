from turtle import Turtle
FONT = ("Arial", 30, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.scoreP1 = 0
        self.scoreP2 = 0
        self.color("white")
        self.goto(x=0, y=250)
        self.write(arg=f"{self.scoreP1}     {self.scoreP2}", move=False, align="center", font=FONT)

    def increase_score_p1(self):
        self.scoreP1 += 1
        self.clear()
        self.write(arg=f"{self.scoreP1}     {self.scoreP2}", move=False, align="center", font=FONT)

    def increase_score_p2(self):
        self.scoreP2 += 1
        self.clear()
        self.write(arg=f"{self.scoreP1}     {self.scoreP2}", move=False, align="center", font=FONT)

#    def increase_score(self):


