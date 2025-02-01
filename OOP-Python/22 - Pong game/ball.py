from turtle import Turtle



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_dir = 1
        self.y_dir = 1
        self.move_speed = 1

    def move(self):
        new_x = self.xcor() + self.x_dir * 10 * self.move_speed
        new_y = self.ycor() + self.y_dir * 8 * self.move_speed
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_dir *= -1

    def paddle_bounce(self):
        self.x_dir *= -1
        self.move_speed *= 1.05
    
    def reset(self):
        self.goto(0, 0)
        self.move_speed = 1
        self.x_dir *= -1
        self.y_dir *= -1
