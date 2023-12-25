from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_func():
    t.circle(20)
    t.forward(50)


screen.listen()
screen.onkey(key='space', fun=move_func)
screen.exitonclick()