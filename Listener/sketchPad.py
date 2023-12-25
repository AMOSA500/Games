from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forward():
    t.color('green')
    t.forward(100)


def move_backward():
    t.color('red')
    t.backward(100)


def turn_right():
    t.color('blue')
    right = t.heading() - 10
    t.setheading(right)


def turn_left():
    t.color('red')
    left = t.heading() + 10
    t.setheading(left)


def draw_circle():
    t.color('black')
    t.circle(100)


def turtle_reset():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.listen()
screen.onkey(key='f', fun=move_forward)
screen.onkey(key='b', fun=move_backward)
screen.onkey(key='r', fun=turn_right)
screen.onkey(key='l', fun=turn_left)
screen.onkey(key='c', fun=draw_circle)
screen.onkey(key='q', fun=turtle_reset)

screen.exitonclick()
