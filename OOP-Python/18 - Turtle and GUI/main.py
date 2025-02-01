from turtle import Turtle, Screen, colormode
import random
import colorgram

colormode(255)
colors = colorgram.extract("20_001.webp", 25)

big_jim = Turtle()
big_jim.penup()
big_jim.speed('fastest')
big_jim.goto((-200,-200))
rgb_colors = []

for color in colors:
    rgb_colors.append((color.rgb[0], color.rgb[1], color.rgb[2]))

def make_painting(height, width):
    for i in range(height):
        for _ in range(width):
            big_jim.dot(20, random.choice(rgb_colors))
            big_jim.forward(50)
            big_jim.dot(20, random.choice(rgb_colors))
        if i % 2 == 0:
            big_jim.left(90)
            big_jim.forward(50)
            big_jim.left(90)
        else:
            big_jim.right(90)
            big_jim.forward(50)
            big_jim.right(90)

make_painting(10, 10)


my_screen = Screen()
my_screen.exitonclick()
