import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.move, key="Up")

game_is_on = True
loops = 0
cars = []

while game_is_on:
    time.sleep(0.1)
    screen.update()
    loops += 1
    if loops % 6 == 0:
        car_manager.create_car()
    car_manager.move_cars()
    # detect collision with a car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
            print("You loose")
    if player.reach_top():
        car_manager.increase_move_distance()
        scoreboard.increase_level()



screen.exitonclick()