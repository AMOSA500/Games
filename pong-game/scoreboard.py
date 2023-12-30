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
        self.r_point = 0
        self.l_point = 0
        self.update_display()

    def update_display(self):
        self.write('0', move=False, align=TEXT_ALIGN, font=('Arial', FONT_SIZE, FONT_TYPE))

    def l_display(self):
        self.clear()
        self.l_point += 1
        self.write(f'{self.l_point}', move=False, align=TEXT_ALIGN, font=('Arial', FONT_SIZE, FONT_TYPE))

    def r_display(self):
        self.clear()
        self.r_point += 1
        self.write(f'{self.r_point}', move=False, align=TEXT_ALIGN, font=('Arial', FONT_SIZE, FONT_TYPE))
