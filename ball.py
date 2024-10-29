from turtle import Turtle
import random

STARTING_HEAD = [i for i in range(9, 171)]


class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("grey")
        self.shape("circle")
        STARTING_HEAD.pop(STARTING_HEAD.index(90))
        self.setheading(random.choice(STARTING_HEAD))
        self.speed(3)
        self.goto(position)

    def move(self):
        x = self.xcor()
        y = self.ycor()

        if y + 10 > 475:
            self.setheading(self.heading() * -1)
        elif x + 10 > 760 or x - 10 < -760:
            self.setheading((self.heading() + 180) * -1)
        self.forward(10)

    def paddle_hit(self, paddlex):
        if paddlex >= self.xcor():
            if 270 <= self.heading()  < 360:
                self.setheading(self.heading() - 180)
            elif 180 < self.heading() < 270:
                self.setheading(self.heading() * -1)
        elif paddlex < self.xcor():
            if 270 <= self.heading()  < 360:
                self.setheading(self.heading() * -1)
            elif 180 < self.heading() < 270:
                self.setheading(self.heading() - 180)
