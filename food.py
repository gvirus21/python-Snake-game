from turtle import Turtle, xcor
import random
from typing import Counter

streach_len=0.7
streach_wid=0.7

class Food(Turtle):

    def __init__(self,score):
        self.score=score
        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=streach_len,stretch_wid=streach_wid)
        self.color("yellow")
        self.speed("fastest")
        
    def refresh(self):
        random_x=random.randint(-260,260)
        random_y=random.randint(-260,260)
        self.goto(random_x,random_y)

    