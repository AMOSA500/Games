from turtle import Turtle
import random

t = Turtle()
t.shape('circle')


def color_make():
    color_code = random.randint(100000, 999999)
    return f'#{color_code}'


direction = [0, 90, 180, 270]
t.pensize(5)
t.speed('fastest')

for _ in range(200):
    t.pencolor(color_make())
    t.forward(50)
    t.setheading(random.choice(direction))
