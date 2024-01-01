from turtle import Turtle

TEXT_ALIGN = 'center'


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.point = 0
        self.high_point = self.read_point_from_file() if self.read_point_from_file() > 0 else 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 275)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score is: {self.point} :: High Score: {self.high_point}', move=False, align=TEXT_ALIGN,
                   font=('Arial', 14, 'normal'))

    def increase_score(self):
        self.point += 1
        self.update_score()

    def reset_score(self):
        if self.point > self.high_point:
            self.high_point = self.point
            self.store_point_in_file()
        self.point = 0
        self.update_score()

    def store_point_in_file(self):
        with open('score.txt', 'w') as file:
            file.write(f'{self.high_point}')

    @staticmethod
    def read_point_from_file():
        with open('score.txt', 'r') as file:
            score = file.readline()
            return int(score)
