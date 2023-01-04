from turtle import Turtle

ALIGNMENT = "center"
FONT_SCORE = ("Verdana", 18, "normal")
FONT_GAME_OVER = ("Verdana", 28, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT_SCORE)

    def refresh(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT_SCORE)

    def finish(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT_GAME_OVER)
