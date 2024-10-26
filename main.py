import turtle as t
from paddle import Paddle


screen = t.Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("white")
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -350))

screen.listen()

screen.onkeypress(paddle.go_right, "Right")
screen.onkeypress(paddle.go_left, "Left")

game_is_on = True

while game_is_on:
    screen.update()


t.mainloop()
