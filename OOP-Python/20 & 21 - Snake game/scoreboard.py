from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.write(f'Score : {self.score}', False, align='center')

    def update_score(self):
        self.clear()
        self.write(f'Score : {self.score}', False, align='center')
    
    def game_over(self):
        self.goto(x=0, y=0)
        self.write('GAME OVER')
        