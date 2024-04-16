from turtle import Screen
from paddle import Paddle
from egg import Egg
from scoreboard import Scoreboard # type: ignore
import time

# Use of virtual environment - python -m venv myenv, then myenv/Script/activate.bat
# Create a Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0) # Turn off animation display on screen

# Create a Paddle
paddle_right = Paddle((370,0),"blue")
paddle_left = Paddle((-370,0),"red")

#create a ball
ball = Egg()

# create a scoreboard
scoreboard = Scoreboard()
    
# Move Paddle up 
screen.listen()
screen.onkey(paddle_right.go_up,"Up")
screen.onkey(paddle_right.go_down,"Down")
screen.onkey(paddle_left.go_up,"w")
screen.onkey(paddle_left.go_down,"s")

while(True):
    time.sleep(0.2)
    screen.update()
    ball.move()
    
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Detect a score on the Right, if paddle misses ball
    if ball.xcor() > 380:
        ball.reset_ball_pos() # Reset ball position
        scoreboard.l_point()
    
    # Detect a score on the Left, if paddle misses ball
    if ball.xcor() < -380:
        ball.reset_ball_pos() # Reset ball position
        scoreboard.r_point()
        
    # Detect collision with paddle
    
    if ball.distance(paddle_right) < 30 and ball.xcor() > 340:
        ball.bounce_x()
    
    if ball.distance(paddle_left) < 30 and ball.xcor() < -340:
        ball.bounce_x()
    
screen.exitonclick()