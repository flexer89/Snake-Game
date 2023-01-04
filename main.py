import time
import snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Initialise objects and variables
game_is_on = True
snake = snake.Snake()
food = Food()
scoreboard = Scoreboard()
current_speed = 0.2

# Key pressing listener
screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")

# main game flow
while game_is_on:
    screen.update()
    time.sleep(current_speed)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.refresh()

        # Speed increase
        if current_speed > 0.05:
            current_speed = current_speed - 0.01

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        scoreboard.finish()
        game_is_on = False

    # Detect collision with a tail
    for tile in snake.tiles[1:]:
        if snake.head.distance(tile) < 10:
            scoreboard.finish()
            game_is_on = False

screen.exitonclick()
