from turtle import Turtle
from turtle import Screen
import random

is_race_on = False
screen = Screen()

screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make a bet", prompt = "Which turtle will win the race? Enter a colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []


j = 0
for i in colors:
    j += 35
    new_turtle = Turtle("turtle")
    new_turtle.color(i)
    new_turtle.penup()
    new_turtle.goto(-220, -100 + j)
    turtles.append(new_turtle)
if user_bet:
    is_race_on = True


while is_race_on:
       for turtle in turtles:
           if turtle.xcor() >220:
                winning_colour = turtle.pencolor()
                if winning_colour == user_bet:
                    print(f"You've won! The {winning_colour} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_colour} turtle is the winner")
                is_race_on = False
           random_distance = random.randint(0, 10)
           turtle.forward(random_distance)


screen.exitonclick()
