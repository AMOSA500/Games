from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos,color) -> None:
        super().__init__()
        self.color(color)
        self.shape("square")
        self.shapesize(5, 1, 5)
        # Move paddle to right
        self.penup()
        self.goto(pos)
    
    # Create movement function
    def go_up(self):
        new_y = self.ycor() + 20 # Move by 20 pace
        self.goto(self.xcor(), new_y) # Keep paddle along current x pos and move to new y pos

    def go_down(self):
        new_y = self.ycor() - 20 # Move by 20 pace
        self.goto(self.xcor(), new_y) # Keep paddle along current x pos and move to new y pos