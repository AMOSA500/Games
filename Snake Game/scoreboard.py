from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 230)
        self.update_scoreboard()
        self.hideturtle()

    def score_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', move=False, align='center', font=('Arial', 8, 'normal'))