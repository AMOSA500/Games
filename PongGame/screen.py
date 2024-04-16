from turtle import Turtle, Screen

# Create a Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("grey")
screen.title("Pong Game")
screen.tracer(0) # Turn off animation display on screen

# Create a Paddle
paddle_right = Turtle()
paddle_right.color("blue")
paddle_right.shape("square")
paddle_right.shapesize(5, 1, 5)

# Move paddle to right
paddle_right.penup()
paddle_right.goto(370,0)



# Create movement function
def go_up():
    new_y = paddle_right.ycor() + 20 # Move by 20 pace
    paddle_right.goto(paddle_right.xcor(), new_y) # Keep paddle along current x pos and move to new y pos

def go_down():
    new_y = paddle_right.ycor() - 20 # Move by 20 pace
    paddle_right.goto(paddle_right.xcor(), new_y) # Keep paddle along current x pos and move to new y pos
    
# Move Paddle up 
screen.listen()
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")

while(True):
    screen.update()
    
screen.exitonclick()