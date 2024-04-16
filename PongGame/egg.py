from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("orange")
        self.shape("circle")
        self.shapesize(1,1)

        # Move self
        self.penup()
        self.goto(360,300)
        