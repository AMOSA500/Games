from turtle import Turtle

DEFAULT_POSITION = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def go_up(self):
        self.forward(20)

    def go_to_start(self):
        self.goto(DEFAULT_POSITION)

    def is_at_finish_point(self):
        if self.ycor() > 290:
            return True
        else:
            return False
