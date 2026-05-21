#import colorgram
import random
#colors = colorgram.extract("image.jpeg",30)
#rgb_color = []

#for i in colors:
    #color_object = i.rgb
    #rgb_color.append((color_object[0], color_object[1], color_object[2]))

from turtle import Turtle
from turtle import Screen

tim = Turtle()
screen = Screen()

color_list =  [(160, 168, 173), (8, 6, 3), (156, 161, 160), (97, 106, 115), (18, 22, 30), (186, 192, 199),
     (112, 102, 81), (104, 109, 106), (152, 147, 133), (7, 3, 5), (236, 210, 121), (19, 24, 21),
     (185, 194, 197), (114, 127, 144), (246, 236, 172), (187, 193, 192), (141, 131, 105), (121, 130, 132),
     (124, 129, 127), (84, 69, 37), (50, 56, 86), (152, 149, 152), (95, 90, 93), (58, 66, 63), (57, 66, 68),
     (129, 126, 127), (79, 52, 59), (71, 61, 58)]

tim.penup()
tim.hideturtle()         
tim.speed("fastest")      

screen.colormode(255)
tim.goto(-350,-300)

for j in range(0,10):
    for i in range(0,10):
        tim.pendown()
        tim.dot(20,random.choice(color_list))
        tim.penup()
        tim.forward(75)
    tim.goto(-350,-300 + 63*(j+1))

screen.exitonclick()
