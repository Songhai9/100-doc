from turtle import Turtle, Screen
import random


my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput("Make your bet", "Which turtle will win the race ?")

rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtles = []
for i in range(7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(rainbow_colors[i])
    new_turtle.goto(x=-230, y=(-130 + i * (42.5)))
    turtles.append(new_turtle)

race_is_on = False
if user_bet:
    race_is_on = True
winner = None

while race_is_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
    for turtle in turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            race_is_on = False


if winner == user_bet:
    print(f"You won, winner is {user_bet}")
else:
    print(f"You lost, winner is {winner}")


my_screen.exitonclick()
