from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('black')
        self.penup()
        self.goto(x=-270, y=270)
        self.write(f'Score : {self.score}', font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f'Score : {self.score}', font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER : SCORE : {self.score}', font=FONT, align="center")
    

