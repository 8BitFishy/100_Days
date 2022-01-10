from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.move_location()

    def move_location(self):
        self.goto(random.randint(-14, 14) * 20, random.randint(-14, 14) * 20)
