from turtle import Turtle


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.remove_blocks = []
        self.hideturtle()
        self.goto(position)
        self.color("white")
        self.update_score()
        self.score = len(self.remove_blocks) * 4

    def update_score(self):
        self.clear()
        self.write(len(self.remove_blocks)*4, align="center", font=("Corier", 80, "normal"))