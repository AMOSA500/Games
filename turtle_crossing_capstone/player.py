from turtle import Turtle

DEFAULT_POSITION = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.setheading(90)
        self.refresh()

    def go_up(self):
        self.forward(20)

    def refresh(self):
        self.goto(DEFAULT_POSITION)
