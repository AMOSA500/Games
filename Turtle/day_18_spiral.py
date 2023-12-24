import turtle as tt
import random

t = tt.Turtle()
t.shape('triangle')
tt.colormode(255)
t.speed('fast')


def set_colors():
    """ Returns rgb colors"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_circle(gap):
    for _ in range(int(360 / gap)):
        t.color(set_colors())
        t.circle(100)
        t.setheading(t.heading() + gap)


draw_circle(10)

screen = tt.Screen()
screen.exitonclick()
