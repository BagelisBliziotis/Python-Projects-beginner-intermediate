from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:
    def __init__(self):
        self.timis = []
        self.create_snake()
        self.head = self.timis[0]

    def create_snake(self):
        for i in range(0,3):
            tim = Turtle("square")
            tim.color("white")
            tim.penup()
            tim.goto(-20 * i, 0)
            self.timis.append(tim)


    def move(self):
        for tim in range(len(self.timis)-1, 0, -1):
            new_x = self.timis[tim-1].xcor()
            new_y = self.timis[tim - 1].ycor()
            self.timis[tim].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
