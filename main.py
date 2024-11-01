import time
import turtle as t
from paddle import Paddle
from ball import Ball
from blocks import Blocks


screen = t.Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -350))
ball = Ball((0, -330))
blocks = Blocks()

screen.listen()

screen.onkeypress(paddle.go_right, "Right")
screen.onkeypress(paddle.go_left, "Left")

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    if ball.ycor() < - 340 and ball.distance(paddle) < 200:
        ball.paddle_hit(paddlex=paddle.xcor())


t.mainloop()
