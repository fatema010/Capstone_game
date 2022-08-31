from turtle import Turtle

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10
Y_AXIS = 270


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_start_again()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_start_again(self):
        self.goto(STARTING_POSITION)

    def is_top_line(self):
        if self.ycor() > Y_AXIS:
            return True
        else:
            return False
