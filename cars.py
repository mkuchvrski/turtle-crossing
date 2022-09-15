from turtle import Turtle
import random

COLORS = ["red", "blue", "green", "yellow", "black", "orange", "purple"]

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.goto(300, random.randint(-240,240))
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=1.5)
        self.color(random.choice(COLORS))
    
    def move_forward(self):
        self.forward(10)
   
            