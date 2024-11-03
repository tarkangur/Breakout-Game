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


def check_collision_with_blocks():
    for block in blocks.all_blocks:
        right, left, top, bot = blocks.block_wall(block)

        if ball.distance(right) < 20 or ball.distance(left) < 20:
            ball.setheading((ball.heading() + 180) * -1)
            block.hideturtle()
            blocks.all_blocks.remove(block)
        elif ball.distance(top) < 20 or ball.distance(bot) < 20:
            ball.setheading(ball.heading() * -1)
            block.hideturtle()
            blocks.all_blocks.remove(block)


game_is_on = True
while game_is_on:
    time.sleep(0.02)
    screen.update()
    ball.move()
    if ball.ycor() < - 340 and ball.distance(paddle) < 200:
        ball.paddle_hit(paddlex=paddle.xcor())

    check_collision_with_blocks()


t.mainloop()
