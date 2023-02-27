import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkeypress(fun=player.move, key="Up")

game_is_on = True
loops = 0
cars = []
while game_is_on:
    loops += 1
    if loops % 6 == 0:
        new_car = CarManager()
        cars.append(new_car)
    for car in cars:
        car.move()
    # detect collision with a car
    for car in cars:
        if player.distance(car) < 25:
            game_is_on = False
            print("You loose")
    time.sleep(0.1)
    screen.update()


screen.exitonclick()