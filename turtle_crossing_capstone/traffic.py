from turtle import Turtle
import random

TRAFFIC_LANE = [-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250]


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.create_cars()

    def create_cars(self):
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.traffic_color()
        self.goto(0, 0)

    def traffic_color(self):
        r = random.randint(0, 255)
        b = random.randint(0, 255)
        g = random.randint(0, 255)
        self.color((r, b, g))

    # def traffic_lane(self):
    #     for lane in TRAFFIC_LANE:
    #         self.go