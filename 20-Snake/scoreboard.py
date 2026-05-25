from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier",24,"normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(-5, 260)
        self.write(f"Score:{self.score}",align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!!" , align =ALIGNMENT, font = FONT)

    def scoring(self):
        self.score += 1
        self.clear()
        self.write(f"Score:{self.score}", align=ALIGNMENT , font= FONT)

