import time
import turtle as t
from paddle import Paddle
from ball import Ball
from blocks import Blocks
from score import Score
from tkinter import Toplevel, Label, Button


screen = t.Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -350))
ball = Ball((0, -330))
blocks = Blocks()
score = Score((650, 350))

screen.listen()

screen.onkeypress(paddle.go_right, "Right")
screen.onkeypress(paddle.go_left, "Left")


def check_collision_with_blocks():
    for block in blocks.all_blocks:
        right, left, top, bot = blocks.block_wall(block)

        if ball.distance(right) < 20 or ball.distance(left) < 20:
            ball.setheading((ball.heading() + 180) * -1)
            score.remove_blocks.append(block)
            block.hideturtle()
            blocks.all_blocks.remove(block)
        elif ball.distance(top) < 20 or ball.distance(bot) < 20:
            ball.setheading(ball.heading() * -1)
            score.remove_blocks.append(block)
            block.hideturtle()
            blocks.all_blocks.remove(block)

def show_popup ():
    popup = Toplevel()
    popup.title("Game Over")
    popup.geometry("200x100")

    message = Label(popup, text=f"Game Over!\nYour Score: {len(score.remove_blocks) * 4}")
    message.pack(pady=10)

    ok_button = Button(popup, text="OK", command=popup.destroy)
    ok_button.pack(pady=5)


game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()
    if ball.ycor() < - 340 and ball.distance(paddle) < 200:
        ball.paddle_hit(paddlex=paddle.xcor())
    elif ball.ycor() < - 360:
        game_is_on = False
        show_popup()
    check_collision_with_blocks()
    score.update_score()


t.mainloop()
