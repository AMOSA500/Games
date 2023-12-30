from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color(self.food_color())
        self.reload_food()

    def reload_food(self):
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 280)
        self.goto((x_cor, y_cor))

    @staticmethod
    def food_color():
        r = random.randint(0, 255)
        b = random.randint(0, 255)
        g = random.randint(0, 255)
        return r, b, g
