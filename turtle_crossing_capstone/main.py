from turtle import Turtle, Screen


# Create the turtle screen
screen = Screen()
screen.title('The Turtle Crossing Capstone Game')
screen.setup(600, 600)
screen.colormode(255)
screen.tracer(0)

car = Turtle()
car.shape('turtle')
car.color('black')
car.penup()
car.setheading(90)
car.goto(0, -280)


is_game_on = True
while is_game_on:
    screen.update()

screen.exitonclick()

