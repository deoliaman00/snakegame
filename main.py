import time
from turtle import Screen, Turtle

from food import Food
from scoreboard import Scoreboard
from snakegame1 import Snakegame1

snakegame1 = Snakegame1()
food = Food()
scoreboard = Scoreboard()

# THIS WAS TO PLACE THE BLACK SCREEN
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# ADDING CONTROLS TO THE FUNCTION
screen.listen()
screen.onkey(snakegame1.up, "Up")
screen.onkey(snakegame1.down, "Down")
screen.onkey(snakegame1.left, "Left")
screen.onkey(snakegame1.right, "Right")

# HERE WE HAVE TRIED TO PLACE
game_is_on = True

# THIS IS THE CODE FOR MOVING FORWARD OF THE SNAKE
# THIS HELPS IN MOVING LEFT RIGHT AS PER US

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snakegame1.move()
    # we need to detect that the snake have might eaten the foood
    # to detect the collision we did this  distance application

    if snakegame1.head.distance(food) < 15:
        food.refresh()
        snakegame1.extend()
        scoreboard.increase_score()
        # DETECTING THAT A SNAKE MIGHT HAVE CROSSED THE WALL
        # FURTHER TELLING THE USER GAME IS OVER
    if snakegame1.head.xcor() > 280 or snakegame1.head.xcor() < -280 or snakegame1.head.ycor() > 280 or snakegame1.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    ## now we want to detect that if they might collide with
    ##the tail then waht to do to exit
    for segment in snakegame1.segments[1:]:
        if snakegame1.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
