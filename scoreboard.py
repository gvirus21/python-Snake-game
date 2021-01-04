from turtle import Turtle, hideturtle

FONT="Cascadia mono"
STYLE="bold"
FONT_WEIGHT=15
class Scoreboard(Turtle):
    def __init__(self,score):
        self.score=score
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-210,250)
        self.updateScoreboard()

    def updateScoreboard(self):
        self.write(f"Score :{self.score}" ,font=(FONT,FONT_WEIGHT,STYLE),align="center",)
    
    def increase_score(self):
        self.score+=1
        self.clear()
        self.updateScoreboard()

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER",font=(FONT,20,STYLE),align="center")
