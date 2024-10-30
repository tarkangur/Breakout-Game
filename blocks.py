import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue"]
LEN = 3.5
WID = 2.0


class Blocks(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=WID, stretch_len=LEN)

    def create_bricks(self):
        pass

