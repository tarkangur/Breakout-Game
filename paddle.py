from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=0.75, stretch_len=17)
        self.penup()
        self.goto(position)

    def go_right(self):
        if self.xcor() < 500:
            new_x = self.xcor() + 200
            self.goto(new_x, self.ycor())

    def go_left(self):
        if self.xcor() > -500:
            new_x = self.xcor() - 200
            self.goto(new_x, self.ycor())
