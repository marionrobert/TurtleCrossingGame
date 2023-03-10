from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.move_distance = 10

    def move(self):
        self.forward(20)

    def reach_top(self):
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
