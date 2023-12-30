from turtle import Turtle

TEXT_ALIGN = 'center'


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.point = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 275)
        self.score()

    def score(self):
        self.write(f'Score is: {self.point}', move=False, align=TEXT_ALIGN, font=('Arial', 16, ''))

    def show_score(self):
        self.point += 1
        self.clear()
        self.write(f'Score is: {self.point}', move=False, align=TEXT_ALIGN, font=('Arial', 16, ''))

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', move=False, align=TEXT_ALIGN, font=('Arial', 16, ''))
