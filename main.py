import time
from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = Car()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.go_up, "Up")
should_continue = True
while should_continue:
    time.sleep(0.1)
    screen.update()
    car.generate_car()
    car.move_car()
    for data in car.car_list:
        if data.distance(player) < 20:
            should_continue = False
            scoreboard.game_over()
    if player.is_top_line():
        player.go_start_again()
        car.level_up()
        scoreboard.increase_level()

screen.exitonclick()
