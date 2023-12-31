from turtle import Turtle
import random

STARTING_MOVE_DISTANCE = 5
LEVEL_UP = 5


class Cars:
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.speed_up = STARTING_MOVE_DISTANCE

    def create_car(self):
        y_cor = random.randint(-250, 250)
        intervals = random.randint(1, 6)
        if intervals % 3 == 0:
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
            car.backward(self.speed_up)

    def increase_speed(self):
        self.speed_up += LEVEL_UP
