from turtle import Turtle
import random


DEFAULT_POSITION = [(-21, 0), (-42, 0), (-63, 0)]


def get_color():
    set_color = ()
    for _ in range(3):
        color = random.randint(0, 255)
        set_color = set_color + (color,)
    return set_color


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        # Create a snake body
        for position in DEFAULT_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake_obj = Turtle('square')
        snake_obj.color(get_color())
        snake_obj.penup()
        snake_obj.goto(position)
        self.segment.append(snake_obj)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for snake in range(len(self.segment) - 1, 0, -1):
            x_cor = self.segment[snake - 1].xcor()
            y_cor = self.segment[snake - 1].ycor()
            self.segment[snake].goto(x_cor, y_cor)
        self.head.forward(20)


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
