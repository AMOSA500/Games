import CreateTurtles as cT
import random
import show_winner as sw


def start_game():
    # Initialisation declaration
    tt_obj = cT.create_turtles()
    tt_obj.make_screen()

    # Variable declaration
    color = tt_obj.color
    is_race_on = False

    # User make a Bet
    choice_color = tt_obj.screen.textinput(title='Turtle Race: ', prompt='Which Turtle will win the race? '
                                                                         'Enter a color - red, orange, yellow, green, blue,'
                                                                         'purple')

    if choice_color.lower() in color:
        is_race_on = True

        # Draw the Finished Line
        cT.draw_finished_line()

        # Create Turtle Racing Object
        turtle_list = tt_obj.create_turtle_racer()

        while is_race_on:
            for tt in turtle_list:
                if tt.xcor() > 230:
                    win_color = tt.pencolor()
                    if win_color == choice_color:
                        sw.show_message(f'The winner is Turtle {win_color} and Wins the race')
                        exit_game = tt_obj.screen.numinput(title='Exit Game', prompt='Enter 1 to restart or 0 to Exit')
                        if exit_game == 1:
                            tt_obj.screen.clear()
                            tt_obj.turtle_list.clear()
                            start_game()
                        else:
                            is_race_on = False
                            tt_obj.screen.bye()
                    else:
                        sw.show_message(f'You lose ({choice_color}). The Turtle {win_color} won the race')
                        exit_game = tt_obj.screen.numinput(title='Exit Game', prompt='Enter 1 to restart or 0 to Exit',
                                                           default=int)
                        if exit_game == 1: # Restart
                            tt_obj.screen.clear()
                            tt_obj.turtle_list.clear()
                            start_game()
                        else:
                            is_race_on = False
                            tt_obj.screen.bye()

                distance = random.randint(0, 10)
                tt.forward(distance)

        tt_obj.screen.exitonclick()

    else:
        print("Select color not in the race")


# Start Game
start_game()
