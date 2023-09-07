from turtle import Turtle

# width = 20, height = 100, x_pos = 350, y_pos = 0


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)

    def go_up(self):
        new_y_up = self.ycor() + 20
        self.goto(self.xcor(), new_y_up)

    def go_down(self):
        new_y_down = self.ycor() - 20
        self.goto(self.xcor(), new_y_down)



