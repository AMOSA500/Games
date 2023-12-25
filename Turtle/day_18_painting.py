import turtle as tt
import random

t = tt.Turtle()
tt.colormode(255)
t.speed('fast')
t.hideturtle()


def set_colors():
    """ Returns rgb colors"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


t.penup()
t.setheading(225)
t.forward(500)
t.setheading(0)
number_of_dots = 100


for x in range(1, number_of_dots+1):
    t.dot(20, set_colors())
    t.forward(50)


    if x % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


screen = tt.Screen()
screen.exitonclick()
