from turtle import Turtle

DISTANCE_MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.color = ['green', 'yellow', 'red']
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x_position = 0
        for index in range(3):
            t = Turtle(shape='square')
            t.penup()
            t.color(self.color[index])
            t.goto(x=x_position, y=0)
            x_position -= 21
            self.segments.append(t)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[seg - 1].xcor()
            y_cor = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x=x_cor, y=y_cor)
        self.head.forward(DISTANCE_MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
