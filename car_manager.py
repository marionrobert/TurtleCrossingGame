from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super(CarManager, self).__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(280, random.randint(-250, 250))
        self.move_distance = STARTING_MOVE_DISTANCE

    def move(self):
        self.forward(self.move_distance)

    def increase_move_distance(self):
        self.move_distance += MOVE_INCREMENT