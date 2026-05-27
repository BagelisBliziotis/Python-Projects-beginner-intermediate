from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.turtlesize(5, 1)
        self.color('white')
        self.penup()
        self.goto(x, y)

    def go_up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(),self.ycor() + 20)
        elif 241 > self.ycor() > 239:
            self.goto(self.xcor(),self.ycor() + 10)
