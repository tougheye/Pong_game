
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong®")
screen.tracer(0)
scoreboard = Scoreboard()
scoreboard.update_scoreboard()


right_paddle = Paddle(x=350, y=0)
left_paddle = Paddle(x=-350, y=0)
ball = Ball()


screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game_is_on = True


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
#Detect Collision and bounce the ball back
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
        ball.move()

#Detect collision with paddle

    if right_paddle.distance(ball) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_hit()
        ball.move()

#Detect ball misses the paddle
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_score += 1
        scoreboard.update_scoreboard()

    elif ball.xcor() < -380:
        ball.reset()
        scoreboard.r_score += 1
        scoreboard.update_scoreboard()


screen.exitonclick()
