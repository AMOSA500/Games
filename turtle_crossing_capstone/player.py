from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.setheading(90)
        self.goto(0, -280)

    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.backward(20)

    def go_left(self):
        self.left(20)

    def go_right(self):
        self.right(20)
