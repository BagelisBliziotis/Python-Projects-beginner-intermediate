from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.direction1 = 1
        self.direction2 = 1
        self.color("white")
        self.move_speed = 0.1
    def reset(self):
        self.goto(0,0)
        self.bounce2()
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + 10*self.direction2, self.ycor() +10*self.direction1)

    def bounce1(self):
        self.direction1 *= -1

    def bounce2(self):
        self.direction2 *= -1
        self.move_speed *= 0.9
