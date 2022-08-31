from turtle import Turtle
import random
COLORS = ["red", "blue", "orange", "purple", "green", "yellow"]
MOVE_DISTANCE = 5
INCREASE_MOVE = 10
class Car:
    def __init__(self):
        self.car_list = []
        self.speed = MOVE_DISTANCE

    def generate_car(self):
        choice = random.randint(1, 5)
        if choice == 1:
            all_car = Turtle("square")
            all_car.shapesize(stretch_wid=1, stretch_len=2)
            all_car.penup()
            all_car.color(random.choice(COLORS))
            y_axis = random.randint(-250, 250)
            all_car.goto(300, y_axis)
            self.car_list.append(all_car)

    def move_car(self):
        for auto in self.car_list:
            auto.backward(self.speed)

    def level_up(self):
        self.speed += INCREASE_MOVE
