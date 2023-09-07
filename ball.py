from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_back(self):
        curr_angle = self.heading()
        new_angle = curr_angle + 90.0
        if 0 < curr_angle < 90 or 180 < curr_angle < 270:
            self.right(new_angle)
            self.forward(10)
        elif 90 < curr_angle < 180 or 270 < curr_angle < 360:
            self.left(new_angle)
            self.forward(10)

    # Angela solution
    def bounce(self):
        self.y_move *= -1

    def paddle_hit(self):
        self.x_move *= -1
        self.move_speed *= 0.2

    def reset(self):
        self.home()
        self.paddle_hit()


