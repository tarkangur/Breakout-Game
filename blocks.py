import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue"]
LEN = 3.5
WID = 2.0


class Blocks:
    def __init__(self):
        self.all_blocks = []
        for y in range(-70, 120, 45):
            for x in range(-730, 731, 73):
                self.add_block(x, y)

    def add_block(self, x, y):
        block = Turtle("square")
        block.penup()
        if y == -70:
            block.color(COLORS[4])
        elif y == -25:
            block.color(COLORS[3])
        elif y == 20:
            block.color(COLORS[2])
        elif y == 65:
            block.color(COLORS[1])
        elif y == 110:
            block.color(COLORS[0])
        block.shapesize(stretch_wid=WID, stretch_len=LEN)
        block.goto(x, y)
        self.all_blocks.append(block)
