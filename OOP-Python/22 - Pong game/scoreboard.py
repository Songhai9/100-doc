from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.goto(x=0, y=280)
        self.write(f'{self.l_score} : {self.r_score}', align='center')
    
    def update_score(self):
        self.clear()
        self.write(f'{self.l_score} : {self.r_score}', align='center')

    def game_over(self, side):
        self.goto(0, 0)
        self.write(f'GAME OVER : winner {'left' if side == 'left' else 'right'} player', align="center")