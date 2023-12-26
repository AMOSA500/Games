from turtle import Turtle, Screen


def draw_finished_line():
    finish_line = Turtle()
    finish_line.penup()
    finish_line.goto(230, 150)
    finish_line.setheading(finish_line.heading() + 270)
    finish_line.pendown()
    finish_line.forward(300)


class create_turtles:
    def __init__(self):
        self.screen = Screen()
        self.color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
        self.turtle_list = []

    def make_screen(self):
        self.screen.setup(width=500, height=500)

    def create_turtle_racer(self):
        y = -150
        for x in self.color:
            t = Turtle(shape='turtle')
            t.penup()
            t.color(x)
            t.goto(x=-230, y=y)
            y += 50
            self.turtle_list.append(t)
        return self.turtle_list
