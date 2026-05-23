from turtle import Turtle
from turtle import Screen

tim = Turtle()
screen = Screen()

screen.listen()

def move_f():
    tim.forward(20)

def move_back():
    tim.backward(20)

def left():
    tim.left(10)

def right():
    tim.right(10)

def clear():
    screen.reset()



screen.onkey(clear,"c")
screen.onkey(left,"a")
screen.onkey(move_f,"w")
screen.onkey(right,"d")
screen.onkey(move_back,"s")



screen.exitonclick()
