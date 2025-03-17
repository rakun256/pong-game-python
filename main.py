from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from screen import ScreenDraw

s = Screen()
s.bgcolor("#0a2a61")
s.setup(width=960, height=720)
s.title("Pong")
s.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
screen_draw = ScreenDraw()
l_score = 0
r_score = 0
scoreboard_l = Scoreboard()
scoreboard_r = Scoreboard()
scoreboard_l.show_board(score=l_score, position=(-100, 200))
scoreboard_r.show_board(score=r_score, position=(100, 200))

s.listen()
s.onkey(l_paddle.go_up, "w")
s.onkey(l_paddle.go_down, "s")
s.onkey(r_paddle.go_up, "Up")
s.onkey(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.distance(r_paddle) < 33 and ball.xcor() > 325 or ball.distance(l_paddle) < 33 and ball.xcor() < -325:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        l_score += 1
        scoreboard_l.show_board(score=l_score, position=(-100, 200))

    if ball.xcor() < -380:
        ball.reset_position()
        r_score += 1
        scoreboard_r.show_board(score=r_score, position=(100, 200))

s.exitonclick()