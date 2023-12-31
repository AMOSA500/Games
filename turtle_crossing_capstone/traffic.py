from turtle import Turtle
import random

STARTING_MOVE_DISTANCE = 5


class Cars():
    def __init__(self):
        super().__init__()
        self.all_cars = []

    def create_car(self):
        y_cor = random.randrange(-250, 250, 10)
        car = Turtle()
        car.penup()
        car.shape('square')
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.color(self.traffic_color())
        car.goto(300, y_cor)
        self.all_cars.append(car)

    @staticmethod
    def traffic_color():
        r = random.randint(0, 255)
        b = random.randint(0, 255)
        g = random.randint(0, 255)
        return r, b, g

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
