from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

paddle1 = Paddle(350, 0)
paddle2 = Paddle(-350, 0)
ball = Ball()
score = Scoreboard()

screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")
score.update()
game_is_on = True
tim = 0.1
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce1()

    if ball.distance(paddle1) < 50 and ball.xcor() >320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        if ball.xcor() > 0 and ball.direction2 >0 or ball.xcor() < 0 < ball.direction1:
            ball.bounce2()

    if ball.xcor() >= 400:
        ball.reset()
        score.l_score += 1
        score.update()
    elif ball.xcor() <= -400:
        ball.reset()
        score.r_score += 1
        score.update()
    ball.move()




screen.exitonclick()
