from turtle_tim import TurtleTim
from turtle import Screen
from cars import Car
import time


screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.bgcolor("white")

turtle = TurtleTim()

game_is_on = True
screen.listen()
screen.onkey(turtle.move_forward, "Up")
screen.onkey(turtle.move_backward, "Down")
i = 0
cars = []
while game_is_on:
    screen.update()
    time.sleep(0.2)
    i += 1
    if i == 6:
        car = Car()
        cars.append(car)
        i = 0

    for car in cars:
        car.move_forward()
        if car.distance(turtle) < 10:
            print("End of game")
        if turtle.ycor() > 280:
            print("Next level") # here have to put recursion