import CreateTurtles as Tt
import random

# Variable declaration
Tt.create_turtles().make_screen()
color = Tt.create_turtles().color
is_race_on = False

# User make a Bet
choice_color = Tt.create_turtles().screen.textinput(title='Turtle Race: ', prompt='Which Turtle will win the race? '
                                                                                  'Enter a color')

# Draw the Finished Line
Tt.draw_finished_line()

# Create Turtle Racing Object
turtle_list = Tt.create_turtles().create_turtle_racer()

if choice_color in color:
    is_race_on = True
else:
    print("Select color not in the race")

while is_race_on:
    for tt in turtle_list:
        if tt.xcor() > 230:
            win_color = tt.pencolor()
            if win_color == choice_color:
                print(f'The winner is Turtle {win_color} and Wins the race')
            else:
                print(f'You lose ({choice_color}). The Turtle {win_color} won the race')
            is_race_on = False

        distance = random.randint(0, 10)
        tt.forward(distance)

Tt.create_turtles().screen.exitonclick()
