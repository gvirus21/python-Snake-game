from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
game_is_on=True
score=0

snake=Snake()

scoreboard=Scoreboard(score)

food=Food(score)

""" actions """

screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")

while game_is_on:

    screen.update()
    snake.move()
    time.sleep(0.1)
    
    
    if snake.head.distance(food)<15:
        """ if food is less than 15px distance from snake head,snake eats food """
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
        score+=1

    if snake.head.xcor() >290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        """ if snake touch outer wall,game is lost """
        scoreboard.game_over()
        game_is_on=False
    
    for segment in snake.segments[1:]:
        """ if snake head make contacts with its body,game is lost """
        if snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()


screen.exitonclick()
