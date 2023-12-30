import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.color((self.ball_color()))
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10

    @staticmethod
    def ball_color():
        r = random.randint(0, 255)
        b = random.randint(0, 255)
        g = random.randint(0, 255)
        return r, b, g

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        self.color((self.ball_color()))
        self.y_move *= -1

    def bounce_x(self):
        self.color((self.ball_color()))
        self.x_move *= -1

    def start_point(self):
        self.clear()
        self.goto(0, 0)
        self.bounce_x()