from turtle import Turtle, Screen
import random
# Turtle Object

color = ['red','orange','yellow','green','blue','purple']
is_race_on = False
turtle_list = []

# Screen Setup
screen = Screen()
screen.setup(width=500, height=500)
choice_color = screen.textinput(title='Turtle Race: ', prompt='Which Turtle will win the race? Enter a color')


finish_line = Turtle()
finish_line.penup()
finish_line.goto(230,150)
finish_line.setheading(finish_line.heading() + 270)
finish_line.pendown()
finish_line.forward(300)

y = -150
for x in color:
    t = Turtle(shape='turtle')
    t.penup()
    t.color(x)
    t.goto(x=-230, y=y)
    y += 50
    turtle_list.append(t)

if choice_color in color:

    is_race_on = True

while is_race_on:
    for tt in turtle_list:
        if tt.xcor() > 230:
            win_color = tt.pencolor()
            if win_color == choice_color:
                print(f'The winner is Turtle {win_color} and Wins the race')
            else:
                print(f'You lose ({choice_color}). The Turtle {win_color} won the race')
            is_race_on = False

        distance = random.randint(0,10)
        tt.forward(distance)


screen.exitonclick()
