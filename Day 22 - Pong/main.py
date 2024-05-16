from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
import time
from ball import Ball


paddle_left = Paddle(x=-350, y=0)
paddle_right = Paddle(x=350, y=0)
ball = Ball()
scoreboard = Scoreboard()
turtle = Turtle()
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)
screen.listen()

screen.onkey(key="Up", fun=paddle_right.up)
screen.onkey(key="Down", fun=paddle_right.down)
screen.onkey(key="w", fun=paddle_left.up)
screen.onkey(key="s", fun=paddle_left.down)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # detect collision with the paddle
    if ((ball.xcor() > 335 or ball.xcor() < -335) and
            (ball.distance(paddle_left) < 50 or ball.distance(paddle_right) < 50)):
        ball.paddle_bounce()

    # detect point
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.increase_score_p1()

    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.increase_score_p2()



screen.exitonclick()
