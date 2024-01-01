from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from tkinter import messagebox


def main():
    # Create a snake Screen
    screen = Screen()
    screen.title('My Snake Game')
    screen.colormode(255)
    screen.setup(600, 600)
    screen.bgcolor('black')
    screen.tracer(False)

    # Create a snake body
    snake = Snake()

    # Create a snake food
    food = Food()

    # Create a snake scoreboard
    scoreboard = ScoreBoard()

    # Create screen listener
    screen.listen()
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')

    is_game_over = True
    while is_game_over:
        screen.update()
        time.sleep(0.2)
        snake.move()

        # Collision with food
        if snake.head.distance(food) < 15:
            food.clear()
            food.reload_food()
            scoreboard.increase_score()
            snake.extend()

        # Collision with walls
        if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
            restart = messagebox.askyesno('Snake Game', 'Hit Wall! Do want to continue?')
            if restart:
                scoreboard.reset_score()
                snake.reset_snake()
                # Continues snake through the wall
                # x_cor = snake.head.xcor()
                # y_cor = snake.head.ycor()
                # if x_cor < 0 or x_cor > 0:
                #     snake.head.goto(x_cor*-1, y_cor)
                # if y_cor < 0 or y_cor > 0:
                #     snake.head.goto(x_cor, y_cor * -1)
            else:
                is_game_over = False
                screen.bye()

        # Collision with snake body
        for seg in snake.segment[1:]:
            if seg.distance(snake.head) < 10:
                restart = messagebox.askyesno('Snake Game', 'Hit Wall! Do want to continue?')
                if restart:
                    scoreboard.reset_score()
                    snake.reset_snake()
                else:
                    is_game_over = False
                    screen.bye()


main()
