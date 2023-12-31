from turtle import Turtle

FONT = ('Courier', 16, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.number = 0
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.display_level()

    def display_level(self):
        self.write(f'Level: {self.number}', move=False, align='Left', font=FONT)

    def next_level(self):
        self.clear()
        self.number += 1
        self.display_level()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write('GAME OVER', move=False, align='center', font=FONT)
