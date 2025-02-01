from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.lenght = len(self.snake_body)

    def create_snake(self):
        for i in range(3):
            turtle = Turtle("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(x=(0 - i * 20), y=0)
            self.snake_body.append(turtle)

    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[i - 1].xcor()
            new_y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def grow(self):
        limb = Turtle('square')
        limb.color('white')
        limb.penup()
        limb.goto(x=self.snake_body[-1].xcor(), y=self.snake_body[-1].ycor())
        self.snake_body.append(limb)
