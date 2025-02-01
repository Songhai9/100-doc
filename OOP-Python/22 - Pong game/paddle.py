from turtle import Turtle

UP = 90

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.goto(x=x, y=y)
        self.setheading(UP)
    
    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)


