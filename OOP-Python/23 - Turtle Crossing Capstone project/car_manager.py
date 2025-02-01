COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape('square')
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.goto(x=250, y=-250 + random.randint(1, 16)*30 )
        self.setheading(180)
        
    

    def move(self, speed_increase):
        self.forward(MOVE_INCREMENT * speed_increase)
    
    def next_level(self):
        self.speed_increase += 0.2
