from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):
        x_cor = random.randint(-230, 230)
        y_cor = random.randint(-230, 230)
        self.goto(x=x_cor, y=y_cor)
