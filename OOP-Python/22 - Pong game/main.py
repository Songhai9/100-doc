from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_one = Paddle(x=350, y=0)
paddle_two = Paddle(-350, 0)
screen.update()
screen.listen()
screen.onkey(fun=paddle_one.up, key="Up")
screen.onkey(fun=paddle_one.down, key="Down")
screen.onkey(fun=paddle_two.up, key="z")
screen.onkey(fun=paddle_two.down, key="s")

ball = Ball()

scoreboard = Scoreboard() 
game_is_on = True

while game_is_on:
    time.sleep(0.05)
    ball.move()
    screen.update()

    # Detect Ball collision with wall
    if (ball.ycor() > 290) or (ball.ycor() < -290):
        ball.wall_bounce()

    # Detect Ball collision with a paddle
    if (ball.distance(paddle_one) < 50 and ball.xcor() > 320) or (
        ball.distance(paddle_two) < 50 and ball.xcor() < -320
    ):
        ball.paddle_bounce()

    # Detect when someone scored

    if (ball.xcor() > 400):
        ball.reset()
        scoreboard.l_score += 1
        scoreboard.update_score()

    if (ball.xcor() < -400):
        ball.reset()
        scoreboard.r_score += 1
        scoreboard.update_score()
    
    if scoreboard.l_score == 3:
        game_is_on = False
        scoreboard.game_over(side='left')
    if scoreboard.r_score == 3:
        game_is_on = False
        scoreboard.game_over(side='right')

screen.exitonclick()
