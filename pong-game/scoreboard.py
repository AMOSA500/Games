from turtle import Turtle

TEXT_ALIGN = 'center'
FONT_SIZE = 38
FONT_TYPE = 'bold'


class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(position)
        self.point = 0
        self.display()

    def display(self):
        self.write(f'{self.point}', move=False, align=TEXT_ALIGN, font=('Arial', FONT_SIZE, FONT_TYPE))

    def increment(self):
        self.clear()
        self.point += 1
        self.write(f'{self.point}', move=False, align=TEXT_ALIGN, font=('Arial', FONT_SIZE, FONT_TYPE))
