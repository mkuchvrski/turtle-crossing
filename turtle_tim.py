from turtle import Turtle


class TurtleTim(Turtle):
    
    def __init__(self): 
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0,-240)

    def move_forward(self):
        self.forward(10)

    def move_backward(self):
        self.backward(10)