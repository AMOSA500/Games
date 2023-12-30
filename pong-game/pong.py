from turtle import Turtle


class Pong(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color(color)
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def go_up(self):
        new_ycor = self.ycor() + 20
        self.goto(self.xcor(), new_ycor)

    def go_down(self):
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(), new_ycor)

    def centerline(self):
        self.hideturtle()
        self.dot(10, 'white')
        self.shapesize(stretch_len=None, stretch_wid=30)